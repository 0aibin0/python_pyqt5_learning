import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow  # 主窗口
from initcode_builder import SceondWindow  # 二窗口
from lk_to_kernel import ThirdWindow  # 三窗口
from shell_tools import controller_main  # 四窗口
from lk_to_bat import FifthWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initbutton()

    def initbutton(self):
        self.commandLinkButton.clicked.connect(self.initcode_builder_fun)
        self.commandLinkButton_2.clicked.connect(self.lk_to_kernel_fun)
        self.commandLinkButton_3.clicked.connect(self.shell_tools_fun)
        self.commandLinkButton_4.clicked.connect(self.lk_to_bat_fun)

    def initcode_builder_fun(self):
        # self.close()
        self.secondwindow = SceondWindow()
        self.secondwindow.show()

    def lk_to_kernel_fun(self):
        # self.close()
        self.thirdwindow = ThirdWindow()
        self.thirdwindow.show()

    def shell_tools_fun(self):
        # self.close()
        self.fourthwindow = controller_main()
        self.fourthwindow.show()

    def lk_to_bat_fun(self):
        self.fifthwindow = FifthWindow()
        self.fifthwindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
