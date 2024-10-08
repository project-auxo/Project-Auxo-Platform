import time
import json
import random
import logging
from queue import Queue
from typing import Dict

import zmq

from auxo_olympus.lib.utils.zhelpers import dump, ensure_is_bytes, ZMQMonitor, get_host_name_ip, strip_of_bytes
from auxo_olympus.lib.utils.mdpeer import PeerPort
import auxo_olympus.lib.utils.MDP as MDP


# TODO: Change so it can handle requests from multiple clients

# MARK: Constants
LOCAL: bool = True      # if running on this machine, use 'ipc://routing.ipc'


class MajorDomoWorker(object):
    HEARTBEAT_LIVENESS = 3
    broker = None
    ctx = None
    service = None

    worker = None
    hearbeat_at = 0
    liveness = 0
    heartbeat = 2500
    reconnect = 2500

    expect_reply = False
    timeout = 2500
    verbose = False

    reply_to = None       # Return address if any

    def __init__(self, broker, service, verbose=False, worker_name=MDP.W_WORKER, own_port=None):
        self.broker: str = broker
        self.own_port: int = own_port if own_port else 5555 + random.randint(1, 20)
        self.service: str = service
        self.verbose = verbose
        if not isinstance(worker_name, bytes):
            agent_name = worker_name.split(".")[0]
            agent_name = agent_name.encode("utf8")
            worker_name = worker_name.encode("utf8")
        else:
            agent_name = worker_name.split(b".")[0]
        self.worker_name: bytes = worker_name      # of format A01.service
        self.agent_name: bytes = agent_name        # of format A01

        self.worker_socket = None
        self.ctx = zmq.Context()
        self.poller = zmq.Poller()

        self.monitor: ZMQMonitor = None
        self._debug = False

        # Inter-worker peer handling
        ip_addr = get_host_name_ip()
        self.endpoint: str = f"tcp://{ip_addr}:{self.own_port}"
        
        self.peers_endpoints: Dict[bytes, str] = {}    # tcp endpoints of peers for the given service
        # Note that self.peer has not been connected to its peers
        self.peer_port: PeerPort = None
        self.peer_request_queue: Queue = Queue()
        self.leader_bool = False
        self.received_request: bool = False

        logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)

        self.reconnect_to_broker()

        if self._debug:
            # Monitoring
            event_filter: str = 'NONE'     # 'ALL' if self.verbose else EVENT_MAP[zmq.EVENT_ACCPETED]
            self.monitor.run(event=event_filter)

    def reconnect_to_broker(self):
        """Connect or reconnect to broker"""
        if self.ctx:
            if self.worker_socket:
                self.poller.unregister(self.worker_socket)
                self.worker_socket.close()

            self.worker_socket = self.ctx.socket(zmq.DEALER)

            # Setup monitor
            if self._debug:
                self.monitor: ZMQMonitor = ZMQMonitor(self.worker_socket)

            self.worker_socket.identity = self.worker_name
            self.worker_socket.linger = 0
            self.worker_socket.connect(self.broker)
            self.poller.register(self.worker_socket, zmq.POLLIN)
            if self.verbose:
                logging.info(f"I: connecting to broker at {self.broker}...")

            # Register service with broker
            self.send_to_broker(MDP.W_READY, self.service, [])

            # If liveness hits zero, queue is considered disconnected
            self.liveness = self.HEARTBEAT_LIVENESS
            self.heartbeat_at = time.time() + 1e-3 * self.heartbeat

    def send_to_broker(self, command, option=None, msg=None):
        """Send message to broker.
        If no msg is provided, creates one internally
        """
        assert self.worker_socket
        if msg is None:
            msg = []
        elif not isinstance(msg, list):
            msg = [msg]

        if option:
            msg = [option] + msg

        msg = ['', MDP.W_WORKER, command] + msg
        msg = ensure_is_bytes(msg)     # ensure that the message is only bytes

        if self.verbose:
            logging.info(f"I: sending {command} to broker")
            dump(msg)
        self.worker_socket.send_multipart(msg)

    def recv(self, reply=None):
        """Send reply, if any, to broker and wait for next request."""

        if reply is not None:
            assert self.reply_to is not None
            try:
                reply = [self.reply_to, ''] + reply
            except TypeError:       # probably trying to concatenate a list with dict
                reply = [self.reply_to, ''] + [reply]
            self.send_to_broker(MDP.W_REPLY, msg=reply)

        while True:
            # Determine whether the peer-port is dead, break if so
            if not self.peer_port_running():
                break

            # Poll socket for a reply, with timeout
            try:
                items = self.poller.poll(self.timeout)
            except (zmq.ZMQError, KeyboardInterrupt):
                break   # Interrupted

            if items:
                msg = self.worker_socket.recv_multipart()
                if self.verbose:
                    logging.info("I: received message from broker: ")
                    dump(msg)

                self.liveness = self.HEARTBEAT_LIVENESS
                # Don't try to handle errors, just assert noisily
                assert len(msg) >= 3

                # msg from broker:
                #   Frame 0: empty
                #   Frame 1: MDPW
                #   Frame 2: x/02 (type request)
                #   Frame 3: options (type dict -- use json loads to unpack)
                #   Frame 4: client addr
                #   Frame 5: empty
                #   Frame 6: client request

                empty = msg.pop(0)
                assert empty == b''
                header = msg.pop(0)
                assert header == MDP.W_WORKER
                command = msg.pop(0)

                out = self.command_handler(command, msg)
                if out:         # request to process?
                    return out

            else:
                self.liveness -= 1
                if self.liveness == 0:
                    if self.verbose:
                        logging.warning("W: disconnected from broker - retrying...")
                    try:
                        time.sleep(1e-3*self.reconnect)
                    except KeyboardInterrupt:
                        break
                    self.reconnect_to_broker()

            # Send HEARTBEAT if it's time
            if time.time() > self.heartbeat_at:
                self.send_to_broker(MDP.W_HEARTBEAT, msg=self.endpoint)
                self.heartbeat_at = time.time() + 1e-3*self.heartbeat

        self.destroy()

    def command_handler(self, command: bytes, msg: list):
        if command == MDP.W_REQUEST:

            # msg:
            # Frame 0: options
            # Frame 1: client_addr
            # Frame 2: empty
            # Frame 3: client request

            self.received_request: bool = True

            # We should pop and save as many addresses as there are
            # up to a null part, but for now, just save one...
            options = msg.pop(0)
            self.reply_to = msg.pop(0)
            empty = msg.pop(0)
            assert empty == b''
            actual_msg = msg.pop(0)

            options: dict = json.loads(options)

            self.leader_bool = options['leader']

            peers_endpoints: Dict[bytes, bytes] = options['peer_endpoints']
            peers_endpoints: Dict[str, str] = strip_of_bytes(peers_endpoints)
            peers_endpoints.pop(self.worker_name.decode('utf8'))      # pop own endpoint
            self.peers_endpoints = peers_endpoints
            # convert dict[str, str] to dict[bytes, str]

            kv_pairs = list(self.peers_endpoints.items())
            self.peers_endpoints.clear()
            for k, v in kv_pairs:
                new_key: bytes = (k+'.peer').encode('utf8')
                self.peers_endpoints[new_key] = v

            # Construct the peer port given that the broker provides endpoints of peers
            if self.peers_endpoints:
                self.peer_port: PeerPort = PeerPort(
                    endpoint=self.endpoint,
                    peer_name=self.worker_name.decode('utf8') + '.peer',
                    peers=self.peers_endpoints,
                    verbose=False
                )

            return actual_msg  # We have a request to process

        elif command == MDP.W_HEARTBEAT:
            # do nothing on the heartbeat
            pass

        elif command == MDP.W_DISCONNECT:
            self.reconnect_to_broker()

        else:
            logging.error("E: invalid input message: ")
            dump(msg)

    def peer_port_running(self) -> bool:
        """ True if the peer-port is still running """
        if self.peer_port:
            return not self.peer_port.shutdown_flag
        return True

    def destroy(self):
        if self._debug:
            self.monitor.stop()

        logging.warning("W: interrupt received, killing worker...")

        self.worker_socket.close()
        self.ctx = None
