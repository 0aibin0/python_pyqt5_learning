"""

1，在子窗口中创建一个信号，并将信号触发与返回按钮绑定。（当按钮按下时，信号触发）
    return_to_main = QtCore.pyqtSignal()  # 定义一个信号
    self.button.clicked.connect(self.return_to_main.emit)  # 点击按钮时发射信号
2，在主函数中的打开子窗口函数中，将触发信号链接到槽函数
    self.child_window.return_to_main.connect(self.return_to_main_window)  # 连接子窗口信号到槽函数
3，定义槽函数，关闭子窗口，显示主窗口
    def return_to_main_window(self):
        self.child_window.close()  # 关闭子窗口
        self.show()  # 显示主窗口

"""

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton


class ChildWindow(QDialog):
    return_to_main = QtCore.pyqtSignal()  # 定义一个信号

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Child Window')
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton('Return to Main Window', self)
        self.button.setGeometry(50, 50, 200, 50)
        self.button.clicked.connect(self.return_to_main.emit)  # 点击按钮时发射信号


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(300, 300, 400, 300)

        self.button = QPushButton('Open Child Window', self)
        self.button.setGeometry(50, 50, 200, 50)
        self.button.clicked.connect(self.open_child_window)

    def open_child_window(self):
        self.child_window = ChildWindow(self)
        self.child_window.return_to_main.connect(self.return_to_main_window)  # 连接子窗口信号到槽函数
        self.child_window.exec_()

    def return_to_main_window(self):
        self.child_window.close()  # 关闭子窗口
        self.show()  # 显示主窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
