# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainw.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(590, 447)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionServices = QAction(MainWindow)
        self.actionServices.setObjectName(u"actionServices")
        self.actionCustom = QAction(MainWindow)
        self.actionCustom.setObjectName(u"actionCustom")
        self.actionDebug = QAction(MainWindow)
        self.actionDebug.setObjectName(u"actionDebug")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 571, 291))
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.servicesTab = QWidget()
        self.servicesTab.setObjectName(u"servicesTab")
        self.servicesReloadButton = QPushButton(self.servicesTab)
        self.servicesReloadButton.setObjectName(u"servicesReloadButton")
        self.servicesReloadButton.setGeometry(QRect(0, 230, 121, 32))
        self.servicesEditButton = QPushButton(self.servicesTab)
        self.servicesEditButton.setObjectName(u"servicesEditButton")
        self.servicesEditButton.setGeometry(QRect(120, 230, 121, 32))
        self.servicesDeleteButton = QPushButton(self.servicesTab)
        self.servicesDeleteButton.setObjectName(u"servicesDeleteButton")
        self.servicesDeleteButton.setGeometry(QRect(240, 230, 121, 32))
        self.servicesLaunchButton = QPushButton(self.servicesTab)
        self.servicesLaunchButton.setObjectName(u"servicesLaunchButton")
        self.servicesLaunchButton.setGeometry(QRect(360, 230, 121, 32))
        self.servicesTable = QTableWidget(self.servicesTab)
        if (self.servicesTable.columnCount() < 4):
            self.servicesTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.servicesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.servicesTable.setObjectName(u"servicesTable")
        self.servicesTable.setGeometry(QRect(0, 0, 561, 231))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.servicesTable.sizePolicy().hasHeightForWidth())
        self.servicesTable.setSizePolicy(sizePolicy)
        self.servicesTable.setFrameShape(QFrame.StyledPanel)
        self.servicesTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.servicesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.servicesTable.setDragDropOverwriteMode(False)
        self.servicesTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.servicesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.servicesTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.servicesTable.setShowGrid(True)
        self.servicesTable.setGridStyle(Qt.SolidLine)
        self.servicesTable.setRowCount(0)
        self.servicesTable.horizontalHeader().setCascadingSectionResizes(False)
        self.servicesTable.horizontalHeader().setStretchLastSection(False)
        self.servicesTable.verticalHeader().setVisible(False)
        self.servicesTable.verticalHeader().setCascadingSectionResizes(False)
        self.servicesTable.verticalHeader().setStretchLastSection(False)
        self.tabWidget.addTab(self.servicesTab, "")
        self.customTab = QWidget()
        self.customTab.setObjectName(u"customTab")
        self.frame = QFrame(self.customTab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 271, 261))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.formLayoutWidget = QWidget(self.frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 10, 271, 60))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.serviceNameLabel = QLabel(self.formLayoutWidget)
        self.serviceNameLabel.setObjectName(u"serviceNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.serviceNameLabel)

        self.authorLabel = QLabel(self.formLayoutWidget)
        self.authorLabel.setObjectName(u"authorLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.authorLabel)

        self.authorLineEdit = QLineEdit(self.formLayoutWidget)
        self.authorLineEdit.setObjectName(u"authorLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.authorLineEdit)

        self.serviceNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.serviceNameLineEdit.setObjectName(u"serviceNameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.serviceNameLineEdit)

        self.descriptionLabel = QLabel(self.frame)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(30, 70, 81, 16))
        self.descriptionPlainTextEdit = QPlainTextEdit(self.frame)
        self.descriptionPlainTextEdit.setObjectName(u"descriptionPlainTextEdit")
        self.descriptionPlainTextEdit.setGeometry(QRect(10, 90, 251, 161))
        self.frame_2 = QFrame(self.customTab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(300, 0, 261, 261))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.agentLaunchFileTextEdit = QTextEdit(self.frame_2)
        self.agentLaunchFileTextEdit.setObjectName(u"agentLaunchFileTextEdit")
        self.agentLaunchFileTextEdit.setGeometry(QRect(10, 40, 241, 171))
        self.agentGenerateButton = QPushButton(self.frame_2)
        self.agentGenerateButton.setObjectName(u"agentGenerateButton")
        self.agentGenerateButton.setGeometry(QRect(0, 220, 260, 32))
        self.agentLaunchFileLabel = QLabel(self.frame_2)
        self.agentLaunchFileLabel.setObjectName(u"agentLaunchFileLabel")
        self.agentLaunchFileLabel.setGeometry(QRect(10, 10, 181, 16))
        self.line = QFrame(self.customTab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(270, 0, 20, 261))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.tabWidget.addTab(self.customTab, "")
        self.debugTab = QWidget()
        self.debugTab.setObjectName(u"debugTab")
        self.debugTextBrowser = QTextBrowser(self.debugTab)
        self.debugTextBrowser.setObjectName(u"debugTextBrowser")
        self.debugTextBrowser.setGeometry(QRect(0, 0, 561, 261))
        self.tabWidget.addTab(self.debugTab, "")
        self.statusTextBrowser = QTextBrowser(self.centralwidget)
        self.statusTextBrowser.setObjectName(u"statusTextBrowser")
        self.statusTextBrowser.setGeometry(QRect(10, 320, 561, 81))
        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(10, 300, 60, 16))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 290, 561, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 590, 22))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionServices)
        self.menuAbout.addAction(self.actionCustom)
        self.menuAbout.addAction(self.actionDebug)

        self.retranslateUi(MainWindow)
        self.agentGenerateButton.clicked.connect(MainWindow.servicesGenerateButtonPressed)
        self.agentGenerateButton.clicked.connect(self.agentLaunchFileTextEdit.clear)
        self.agentGenerateButton.clicked.connect(self.descriptionPlainTextEdit.clear)
        self.agentGenerateButton.clicked.connect(self.authorLineEdit.clear)
        self.agentGenerateButton.clicked.connect(self.serviceNameLineEdit.clear)
        self.servicesReloadButton.clicked.connect(MainWindow.populateTable)
        self.servicesLaunchButton.clicked.connect(MainWindow.launchServiceExe)
        self.servicesDeleteButton.clicked.connect(MainWindow.deleteServiceExe)
        self.servicesEditButton.clicked.connect(MainWindow.editServiceExe)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Project Auxo - Mount Olympus", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionServices.setText(QCoreApplication.translate("MainWindow", u"Services", None))
        self.actionCustom.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.actionDebug.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.servicesReloadButton.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.servicesEditButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.servicesDeleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.servicesLaunchButton.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        ___qtablewidgetitem = self.servicesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Service Name", None));
        ___qtablewidgetitem1 = self.servicesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Author", None));
        ___qtablewidgetitem2 = self.servicesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem3 = self.servicesTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Last Modified", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.servicesTab), QCoreApplication.translate("MainWindow", u"Services", None))
        self.serviceNameLabel.setText(QCoreApplication.translate("MainWindow", u"Service Name:", None))
        self.authorLabel.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.agentGenerateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(tooltip)
        self.agentLaunchFileLabel.setToolTip(QCoreApplication.translate("MainWindow", u"Use help to see the correct structure for this file", None))
#endif // QT_CONFIG(tooltip)
        self.agentLaunchFileLabel.setText(QCoreApplication.translate("MainWindow", u"Agent Launch File (optional):", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customTab), QCoreApplication.translate("MainWindow", u"Custom", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.debugTab), QCoreApplication.translate("MainWindow", u"Debug", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

