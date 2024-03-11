from PyQt5.QtWidgets import QMainWindow
from ui_thirdwindow import Ui_MainWindow


class Thirdwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Thirdwindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.pushButton_2.clicked.connect(self.returnmainwindow_3)

    def returnmainwindow_3(self):
        self.close()
        # 下面未调用
        if self.parent:
            self.parent.show()