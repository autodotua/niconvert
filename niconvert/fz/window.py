# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\autod\Documents\GitHub\niconvert\niconvert\fz\qt\window.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 813)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(150, 30, 481, 251))
        self.groupBox.setObjectName("groupBox")
        self.btnDownloadXml = QtWidgets.QPushButton(self.groupBox)
        self.btnDownloadXml.setEnabled(True)
        self.btnDownloadXml.setGeometry(QtCore.QRect(370, 210, 93, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDownloadXml.sizePolicy().hasHeightForWidth())
        self.btnDownloadXml.setSizePolicy(sizePolicy)
        self.btnDownloadXml.setObjectName("btnDownloadXml")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 20, 442, 187))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtAv = QtWidgets.QPlainTextEdit(self.widget)
        self.txtAv.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtAv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtAv.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.txtAv.setObjectName("txtAv")
        self.horizontalLayout.addWidget(self.txtAv)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtXml = QtWidgets.QPlainTextEdit(self.widget)
        self.txtXml.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtXml.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtXml.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.txtXml.setObjectName("txtXml")
        self.horizontalLayout_2.addWidget(self.txtXml)
        self.btnBrowseXml = QtWidgets.QPushButton(self.widget)
        self.btnBrowseXml.setObjectName("btnBrowseXml")
        self.horizontalLayout_2.addWidget(self.btnBrowseXml)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1066, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "下载"))
        self.btnDownloadXml.setText(_translate("MainWindow", "下载XML文件"))
        self.label.setText(_translate("MainWindow", "链接/AV号："))
        self.label_2.setText(_translate("MainWindow", "保存位置："))
        self.btnBrowseXml.setText(_translate("MainWindow", "浏览.."))
        self.menu.setTitle(_translate("MainWindow", "关于"))
        self.action.setText(_translate("MainWindow", "关于"))


