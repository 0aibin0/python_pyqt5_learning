from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel
from ui_lk_to_kernel import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QTimer, QDateTime


class ThirdWindow(QMainWindow, Ui_MainWindow):
    return_to_main = pyqtSignal()

    def __init__(self, parent=None):
        super(ThirdWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.setWindowTitle("lk_to_kernel")
        self.textEdit.setPlaceholderText("Enter lk code (e.g. 0x1a,0x2b,0x3c,0x4d)")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setPlaceholderText("generate kernel code (e.g. 1a 2b 3c 4d)")

        self.lab = QLabel("AIBIN", self)
        self.statusbar.addPermanentWidget(self.lab)
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTimeCurrent)
        self.timer.start()

        self.pushButton.clicked.connect(self.lk_to_kernel)
        self.pushButton_2.clicked.connect(self.return_to_main.emit)

    def showTimeCurrent(self):
        d = QDateTime.currentDateTime()
        text = d.toString("yyyy-MM-dd HH:mm:ss")
        self.statusbar.showMessage(text, 0)

    def lk_to_kernel(self):
        # 获取输入文本框中的文本
        self.textEdit = self.textEdit.toPlainText()

        # 移除文本中的"0x"前缀
        input_text = self.textEdit.replace("0x", "")

        # 按行分割文本
        lines = input_text.split('\n')

        # 转换每行中的十六进制值，并将它们连接成一行
        output_lines = []
        for line in lines:
            # 按逗号分割每行中的值
            values = line.split(',')
            # 移除每个值前后的空格
            values = [value.strip() for value in values]
            # 获取值的数量
            col_count = len(values)

            # 连接值，并在需要时添加空格以保持每列宽度一致
            output_line = ' '.join(values).ljust(col_count * 3).rstrip()  # 假设每个十六进制值占用3个字符宽度

            output_lines.append(output_line)

            # 显示转换后的文本
        self.textEdit_2.setPlainText('\n'.join(output_lines))
