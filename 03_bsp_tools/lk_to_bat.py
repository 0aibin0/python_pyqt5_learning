from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel
from ui_lk_to_bat import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QTimer, QDateTime


class FifthWindow(QMainWindow, Ui_MainWindow):
    return_to_main = pyqtSignal()

    def __init__(self, parent=None):
        super(FifthWindow, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.setWindowTitle("lk_to_bat")
        self.setWindowIcon(QIcon('icon_img/转换.png'))
        self.textEdit.setPlaceholderText("Enter lk initcode (e.g. 0x--,0x--,0x--,0x--,0x--)")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setPlaceholderText("generate bat code \n(e.g. adb shell echo \"0x01 > "
                                           "/sys/class/display/dsi/dcs_write\")")

        self.lab = QLabel("AIBIN", self)
        self.statusbar.addPermanentWidget(self.lab)
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTimeCurrent)
        self.timer.start()

        self.pushButton.clicked.connect(self.lk_to_bat)
        self.pushButton_2.clicked.connect(self.return_to_main.emit)

    def showTimeCurrent(self):
        d = QDateTime.currentDateTime()
        text = d.toString("yyyy-MM-dd HH:mm:ss")
        self.statusbar.showMessage(text, 0)

    def lk_to_bat(self):
        # 获取输入文本框中的文本
        self.textEdit = self.textEdit.toPlainText()
        # 按行分割文本
        lines = self.textEdit.split('\n')

        # 转换每行中的十六进制值，并在每行前添加命令前缀和后缀
        output_lines = []

        # 在所有行之前添加特定的第一行
        first_line = "adb shell echo \"0x01 > /sys/class/display/dsi/dcs_write\""
        output_lines.append(first_line)

        for line in lines:
            # 按逗号分割每行中的值
            values = line.split(',')
            # 移除每个值前后的空格
            values = [value.strip() for value in values]

            # 删除每行的前四个值
            values = values[4:]

            # 如果还有剩余的值，则构建输出行
            if values:
                # 连接值，并在需要时添加空格以保持每列宽度一致
                # 假设每个十六进制值占用3个字符宽度
                output_line = ' '.join(values).ljust(len(values) * 3).rstrip()

                # 在每行的开始和结束添加指定的命令前缀和后缀
                # 注意这里使用了双重引号来确保整个命令字符串是正确的
                output_line = f"adb shell echo \"{output_line} > /sys/class/display/dsi/dcs_write\""

                output_lines.append(output_line)

        output_lines.append("pause")
        # 显示转换后的文本
        self.textEdit_2.setPlainText('\n'.join(output_lines))
