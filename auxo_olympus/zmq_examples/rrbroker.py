# Request reply broker

import zmq

context = zmq.Context()
frontend = context.socket(zmq.ROUTER)
backend = context.socket(zmq.DEALER)
frontend.bind("tcp://*:5559")
backend.bind("tcp://*:5560")

# Initialize the poll set
poller = zmq.Poller()
poller.register(frontend, zmq.POLLIN)
poller.register(backend, zmq.POLLIN)


while True:
    socks = dict(poller.poll())

    if socks.get(frontend) == zmq.POLLIN:
        message = frontend.recv()
        print("Message", message)
        more = frontend.getsockopt(zmq.RCVMORE)
        if more:
            backend.send(message, zmq.SNDMORE)
        else:
            backend.send(message)

    if socks.get(backend) == zmq.POLLIN:
        message = backend.recv()
        more = backend.getsockopt(zmq.RCVMORE)
        if more:
            frontend.send(message, zmq.SNDMORE)
        else:
            frontend.send(message)
