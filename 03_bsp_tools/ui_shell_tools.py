# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_shell_tools.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 492)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 631, 121))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(500, 30, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(450, 29, 41, 21))
        self.label.setObjectName("label")
        self.cmdpath = QtWidgets.QLineEdit(self.groupBox)
        self.cmdpath.setGeometry(QtCore.QRect(50, 30, 381, 20))
        self.cmdpath.setObjectName("cmdpath")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(13, 30, 31, 20))
        self.label_2.setObjectName("label_2")
        self.cmds = QtWidgets.QLineEdit(self.groupBox)
        self.cmds.setGeometry(QtCore.QRect(50, 70, 381, 20))
        self.cmds.setObjectName("cmds")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(13, 70, 31, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(450, 70, 41, 21))
        self.label_4.setObjectName("label_4")
        self.splitsymbol = QtWidgets.QLineEdit(self.groupBox)
        self.splitsymbol.setGeometry(QtCore.QRect(500, 70, 71, 20))
        self.splitsymbol.setObjectName("splitsymbol")
        self.send = QtWidgets.QPushButton(self.groupBox)
        self.send.setGeometry(QtCore.QRect(580, 30, 41, 61))
        self.send.setObjectName("send")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 230, 631, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 611, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 130, 631, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.openfile = QtWidgets.QPushButton(self.groupBox_3)
        self.openfile.setGeometry(QtCore.QRect(440, 20, 75, 23))
        self.openfile.setObjectName("openfile")
        self.OUTPUTASFILE = QtWidgets.QCheckBox(self.groupBox_3)
        self.OUTPUTASFILE.setGeometry(QtCore.QRect(440, 60, 81, 21))
        self.OUTPUTASFILE.setObjectName("OUTPUTASFILE")
        self.startconvert = QtWidgets.QPushButton(self.groupBox_3)
        self.startconvert.setGeometry(QtCore.QRect(520, 20, 101, 61))
        self.startconvert.setObjectName("startconvert")
        self.filepath = QtWidgets.QLineEdit(self.groupBox_3)
        self.filepath.setGeometry(QtCore.QRect(50, 20, 381, 20))
        self.filepath.setObjectName("filepath")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(13, 20, 31, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(250, 60, 51, 21))
        self.label_6.setObjectName("label_6")
        self.startindex = QtWidgets.QLineEdit(self.groupBox_3)
        self.startindex.setGeometry(QtCore.QRect(300, 60, 71, 20))
        self.startindex.setObjectName("startindex")
        self.SWAP = QtWidgets.QCheckBox(self.groupBox_3)
        self.SWAP.setGeometry(QtCore.QRect(380, 60, 51, 21))
        self.SWAP.setObjectName("SWAP")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(568, 429, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Command"))
        self.label.setText(_translate("MainWindow", "方  法"))
        self.label_2.setText(_translate("MainWindow", "路径"))
        self.label_3.setText(_translate("MainWindow", "命令"))
        self.label_4.setText(_translate("MainWindow", "分隔符"))
        self.send.setText(_translate("MainWindow", "Send"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Log"))
        self.groupBox_3.setTitle(_translate("MainWindow", "zcv-converter"))
        self.openfile.setText(_translate("MainWindow", "打开文件"))
        self.OUTPUTASFILE.setText(_translate("MainWindow", "以文件输出"))
        self.startconvert.setText(_translate("MainWindow", "START"))
        self.label_5.setText(_translate("MainWindow", "路径"))
        self.label_6.setText(_translate("MainWindow", "起始行列"))
        self.SWAP.setText(_translate("MainWindow", "SWAP"))
        self.pushButton.setText(_translate("MainWindow", "返回主菜单"))
