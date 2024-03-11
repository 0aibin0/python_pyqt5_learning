import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    ui = MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
