import time

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
# from .ui_mainwindow import Ui_MainWindow

from .qthread import Ui_MainWindow
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.progressBar.setAlignment(Qt.AlignHCenter)
        self.thread = Worker()
        self.thread.sig.connect(self.updateLabel)

        self.pushButton_2.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.thread.start()

    def updateLabel(self, text):
        self.label_2.setText(text)


class Worker(QThread):
    sig = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.count = 0
        self.flag = True

    def run(self):

        while True:
            time.sleep(1)
            self.count += 1
            if self.count % 5 == 0:
                self.sig.emit(f"已执行{self.count}秒")
