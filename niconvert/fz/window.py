# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\autod\Documents\GitHub\niconvert\niconvert\fz\window.ui'
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
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnDownloadXml = QtWidgets.QPushButton(self.groupBox)
        self.btnDownloadXml.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDownloadXml.sizePolicy().hasHeightForWidth())
        self.btnDownloadXml.setSizePolicy(sizePolicy)
        self.btnDownloadXml.setObjectName("btnDownloadXml")
        self.gridLayout.addWidget(self.btnDownloadXml, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btnBrowseXmlOutput = QtWidgets.QPushButton(self.groupBox)
        self.btnBrowseXmlOutput.setObjectName("btnBrowseXmlOutput")
        self.gridLayout.addWidget(self.btnBrowseXmlOutput, 1, 2, 1, 1)
        self.txtDownloadOutput = QtWidgets.QLineEdit(self.groupBox)
        self.txtDownloadOutput.setClearButtonEnabled(True)
        self.txtDownloadOutput.setObjectName("txtDownloadOutput")
        self.gridLayout.addWidget(self.txtDownloadOutput, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.txtAv = QtWidgets.QLineEdit(self.groupBox)
        self.txtAv.setClearButtonEnabled(True)
        self.txtAv.setObjectName("txtAv")
        self.gridLayout.addWidget(self.txtAv, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.btnBrowseConvertOutput = QtWidgets.QPushButton(self.groupBox_2)
        self.btnBrowseConvertOutput.setAutoFillBackground(False)
        self.btnBrowseConvertOutput.setObjectName("btnBrowseConvertOutput")
        self.gridLayout_2.addWidget(self.btnBrowseConvertOutput, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.btnConvert = QtWidgets.QPushButton(self.groupBox_2)
        self.btnConvert.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConvert.sizePolicy().hasHeightForWidth())
        self.btnConvert.setSizePolicy(sizePolicy)
        self.btnConvert.setObjectName("btnConvert")
        self.gridLayout_2.addWidget(self.btnConvert, 2, 2, 1, 1)
        self.btnBrowseConvertInput = QtWidgets.QPushButton(self.groupBox_2)
        self.btnBrowseConvertInput.setObjectName("btnBrowseConvertInput")
        self.gridLayout_2.addWidget(self.btnBrowseConvertInput, 0, 2, 1, 1)
        self.txtConvertInput = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtConvertInput.setClearButtonEnabled(True)
        self.txtConvertInput.setObjectName("txtConvertInput")
        self.gridLayout_2.addWidget(self.txtConvertInput, 0, 1, 1, 1)
        self.txtConvertOutput = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtConvertOutput.setClearButtonEnabled(True)
        self.txtConvertOutput.setObjectName("txtConvertOutput")
        self.gridLayout_2.addWidget(self.txtConvertOutput, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chkDisableTop = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkDisableTop.setObjectName("chkDisableTop")
        self.horizontalLayout_2.addWidget(self.chkDisableTop)
        self.chkDisableBottom = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkDisableBottom.setObjectName("chkDisableBottom")
        self.horizontalLayout_2.addWidget(self.chkDisableBottom)
        self.chkDisableGuest = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkDisableGuest.setObjectName("chkDisableGuest")
        self.horizontalLayout_2.addWidget(self.chkDisableGuest)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 2, 1)
        self.txtFilter = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtFilter.setObjectName("txtFilter")
        self.gridLayout_3.addWidget(self.txtFilter, 0, 1, 1, 1)
        self.btnBrowseFilter = QtWidgets.QPushButton(self.groupBox_3)
        self.btnBrowseFilter.setObjectName("btnBrowseFilter")
        self.gridLayout_3.addWidget(self.btnBrowseFilter, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 6, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)
        self.txtMarginBottom = QtWidgets.QSpinBox(self.groupBox_4)
        self.txtMarginBottom.setObjectName("txtMarginBottom")
        self.gridLayout_7.addWidget(self.txtMarginBottom, 7, 1, 1, 1)
        self.txtDropOffset = QtWidgets.QSpinBox(self.groupBox_4)
        self.txtDropOffset.setMaximum(10)
        self.txtDropOffset.setProperty("value", 2)
        self.txtDropOffset.setObjectName("txtDropOffset")
        self.gridLayout_7.addWidget(self.txtDropOffset, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 5, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 4, 0, 1, 1)
        self.cbbFont = QtWidgets.QFontComboBox(self.groupBox_4)
        self.cbbFont.setEditable(True)
        self.cbbFont.setObjectName("cbbFont")
        self.gridLayout_7.addWidget(self.cbbFont, 1, 1, 1, 1)
        self.txtFontSize = QtWidgets.QSpinBox(self.groupBox_4)
        self.txtFontSize.setMaximum(100)
        self.txtFontSize.setSingleStep(5)
        self.txtFontSize.setProperty("value", 30)
        self.txtFontSize.setObjectName("txtFontSize")
        self.gridLayout_7.addWidget(self.txtFontSize, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 7, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 7, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 2, 2, 1, 1)
        self.txtMaxLines = QtWidgets.QSpinBox(self.groupBox_4)
        self.txtMaxLines.setMaximum(10)
        self.txtMaxLines.setProperty("value", 4)
        self.txtMaxLines.setObjectName("txtMaxLines")
        self.gridLayout_7.addWidget(self.txtMaxLines, 2, 1, 1, 1)
        self.txtSpeedOffset = QtWidgets.QSpinBox(self.groupBox_4)
        self.txtSpeedOffset.setMinimum(-10)
        self.txtSpeedOffset.setMaximum(10)
        self.txtSpeedOffset.setObjectName("txtSpeedOffset")
        self.gridLayout_7.addWidget(self.txtSpeedOffset, 4, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chkTimeOffsetNegetive = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkTimeOffsetNegetive.setObjectName("chkTimeOffsetNegetive")
        self.horizontalLayout_4.addWidget(self.chkTimeOffsetNegetive)
        self.txtTimeOffset = QtWidgets.QSpinBox(self.groupBox_4)
        self.txtTimeOffset.setObjectName("txtTimeOffset")
        self.horizontalLayout_4.addWidget(self.txtTimeOffset)
        self.horizontalLayout_4.setStretch(1, 1)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 5, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 4, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.groupBox_4)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rbtnSync = QtWidgets.QRadioButton(self.frame)
        self.rbtnSync.setChecked(True)
        self.rbtnSync.setObjectName("rbtnSync")
        self.horizontalLayout_3.addWidget(self.rbtnSync)
        self.rbtnAsync = QtWidgets.QRadioButton(self.frame)
        self.rbtnAsync.setObjectName("rbtnAsync")
        self.horizontalLayout_3.addWidget(self.rbtnAsync)
        self.gridLayout_7.addWidget(self.frame, 3, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 8, 0, 1, 1)
        self.txtStyle = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtStyle.setClearButtonEnabled(True)
        self.txtStyle.setObjectName("txtStyle")
        self.gridLayout_7.addWidget(self.txtStyle, 8, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton, 8, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtLog = QtWidgets.QTextEdit(self.groupBox_5)
        self.txtLog.setObjectName("txtLog")
        self.horizontalLayout.addWidget(self.txtLog)
        self.horizontalLayout_5.addWidget(self.groupBox_5)
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
        self.cbbFont.setCurrentIndex(411)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BiliBili弹幕下载&转换"))
        self.groupBox.setTitle(_translate("MainWindow", "下载"))
        self.btnDownloadXml.setText(_translate("MainWindow", "下载XML文件"))
        self.label_2.setText(_translate("MainWindow", "输出："))
        self.btnBrowseXmlOutput.setText(_translate("MainWindow", "浏览.."))
        self.txtDownloadOutput.setPlaceholderText(_translate("MainWindow", "自动"))
        self.label.setText(_translate("MainWindow", "链接/AV号："))
        self.groupBox_2.setTitle(_translate("MainWindow", "ASS输入/输出"))
        self.label_4.setText(_translate("MainWindow", "输出："))
        self.btnBrowseConvertOutput.setText(_translate("MainWindow", "浏览.."))
        self.label_3.setText(_translate("MainWindow", "输入："))
        self.btnConvert.setText(_translate("MainWindow", "导出"))
        self.btnBrowseConvertInput.setText(_translate("MainWindow", "浏览.."))
        self.groupBox_3.setTitle(_translate("MainWindow", "弹幕选项"))
        self.label_5.setText(_translate("MainWindow", "屏蔽："))
        self.chkDisableTop.setText(_translate("MainWindow", "顶部弹幕"))
        self.chkDisableBottom.setText(_translate("MainWindow", "底部弹幕"))
        self.chkDisableGuest.setText(_translate("MainWindow", "游客弹幕"))
        self.label_6.setText(_translate("MainWindow", "过滤文件："))
        self.btnBrowseFilter.setText(_translate("MainWindow", "浏览.."))
        self.groupBox_4.setTitle(_translate("MainWindow", "字幕选项"))
        self.label_16.setText(_translate("MainWindow", "秒"))
        self.label_12.setText(_translate("MainWindow", "布局算法："))
        self.label_9.setText(_translate("MainWindow", "字体："))
        self.label_8.setText(_translate("MainWindow", "‰"))
        self.label_20.setText(_translate("MainWindow", "秒"))
        self.label_13.setText(_translate("MainWindow", "速度调整："))
        self.cbbFont.setCurrentText(_translate("MainWindow", "微软雅黑"))
        self.label_15.setText(_translate("MainWindow", "丢弃偏移："))
        self.label_10.setText(_translate("MainWindow", "最大行数："))
        self.label_18.setText(_translate("MainWindow", "%"))
        self.label_17.setText(_translate("MainWindow", "底部留白："))
        self.label_11.setText(_translate("MainWindow", "行"))
        self.chkTimeOffsetNegetive.setText(_translate("MainWindow", "-"))
        self.label_7.setText(_translate("MainWindow", "字体大小："))
        self.label_19.setText(_translate("MainWindow", "时间偏移"))
        self.label_14.setText(_translate("MainWindow", "秒"))
        self.rbtnSync.setText(_translate("MainWindow", "速度同步"))
        self.rbtnAsync.setText(_translate("MainWindow", "速度异步"))
        self.label_21.setText(_translate("MainWindow", "样式文件："))
        self.txtStyle.setPlaceholderText(_translate("MainWindow", "默认"))
        self.pushButton.setText(_translate("MainWindow", "浏览.."))
        self.groupBox_5.setTitle(_translate("MainWindow", "日志"))
        self.menu.setTitle(_translate("MainWindow", "关于"))
        self.action.setText(_translate("MainWindow", "关于"))


