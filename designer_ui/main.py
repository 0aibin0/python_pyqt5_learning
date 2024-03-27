import sys
import os
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QFileDialog

from test import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.actionxinjian.triggered.connect(self.showmain)

        self.lab = QLabel("AIBIN", self)
        self.statusBar.addPermanentWidget(self.lab)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showtime)
        self.timer.start()

        self.pushButton.clicked.connect(self.openfile)
        self.pushButton_2.clicked.connect(self.openfileD)


    def openfile(self):
        self.file = QFileDialog()
        self.file.setFileMode(QFileDialog.ExistingFiles)
        self.file.setDirectory("D:\\")
        self.file.setNameFilter("图片文件(*.jpg *.png)")

        if self.file.exec_():
            self.listWidget.addItems(self.file.selectedFiles())
            self.lineEdit.setText("文件选取成功")

    def openfileD(self):
        self.fileD = QFileDialog.getExistingDirectory(None, "选择文件夹路径", os.getcwd())
        self.lineEdit_2.setText(self.fileD)
        self.list = os.listdir(self.fileD)
        self.listWidget.clear()
        self.listWidget.addItems(self.list)


    def showtime(self):
        d = QDateTime.currentDateTime()
        text = d.toString("yyyy-MM-dd HH:mm:ss")
        self.statusBar.showMessage(text, 0)

    def showmain(self):
        QMessageBox.information(self.parent, "提示", "你选择的是新建", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
