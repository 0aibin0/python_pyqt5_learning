from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton
from QTimer_test import *
from PyQt5.QtGui import QIcon, QPixmap


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        icon = QIcon()
        icon.addPixmap(QPixmap('qt.jpg'))
        self.setWindowIcon(icon)

        self.timer = QTimer()
        self.count = 0
        self.timer.timeout.connect(self.showNum)

    def showNum(self):
        self.count += 1
        print(self.count)
        # 获取系统当前时间
        time = QDateTime.currentDateTime()
        print(time)

    def start_timer(self):
        self.timer.start(1000)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(True)

    def stop_timer(self):
        self.timer.stop()
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(False)
