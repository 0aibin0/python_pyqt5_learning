import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow  # 主窗口
from secondwindow import SecondWindow
from thirdwindow import Thirdwindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.showSecondWindow)
        self.pushButton_2.clicked.connect(self.showThirdWindow)

    def showSecondWindow(self):
        # self.close()
        self.secw = SecondWindow()
        self.secw.show()

    def showThirdWindow(self):
        self.thrw = Thirdwindow()
        self.thrw.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


