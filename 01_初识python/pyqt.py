import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('简单的PyQt示例')
        self.setGeometry(300, 300, 300, 200)

        # 创建一个按钮
        btn = QPushButton('点击我', self)
        btn.move(100, 100)
        btn.clicked.connect(self.showDialog)

    def showDialog(self):
        QMessageBox.information(self, '消息', '你点击了按钮！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
