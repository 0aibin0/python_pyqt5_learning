from PyQt5.QtWidgets import QMainWindow
from ui_secondwindow import Ui_MainWindow


class SecondWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.pushButton_2.clicked.connect(self.returnmainwindow_2)

    def returnmainwindow_2(self):
        self.close()
        # 下面未调用
        if self.parent:
            self.parent.show()
