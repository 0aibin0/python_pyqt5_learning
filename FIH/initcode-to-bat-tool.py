import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QSplitter, QPushButton, QVBoxLayout, QWidget, QDialog, \
    QMessageBox
from PyQt5.QtCore import Qt


class HexConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('initcode-to-bat-tool')  # 设置窗口标题
        self.setGeometry(300, 300, 600, 400)  # 设置窗口初始位置和大小

        # 创建分割器并设置为水平方向
        self.splitter = QSplitter(Qt.Horizontal)

        # 创建输入文本框，并设置占位符文本
        self.input_text = QTextEdit(self)
        self.input_text.setPlaceholderText("Enter lk initcode (e.g. 0x--,0x--,0x--,0x--,0x--)")

        # 创建转换按钮，并连接其clicked信号到convert_hex槽函数
        self.convert_button = QPushButton("Convert", self)
        self.convert_button.clicked.connect(self.convert_hex)

        # 创建输出文本框，并设置为只读
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText("generate bat code \n(e.g. adb shell echo \"0x01 > "
                                            "/sys/class/display/dsi/dcs_write\")")
        # 创建垂直布局，并添加分割器和转换按钮
        layout = QVBoxLayout()
        layout.addWidget(self.splitter)
        layout.addWidget(self.convert_button)

        # 创建中心部件，并设置其布局
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 将输入和输出文本框添加到分割器中
        self.splitter.addWidget(self.input_text)
        self.splitter.addWidget(self.output_text)

        # 设置分割器中两个部件的初始大小
        self.splitter.setSizes([self.size().width() // 2, self.size().width() // 2])

    def convert_hex(self):
        # 获取输入文本框中的文本
        input_text = self.input_text.toPlainText()
        # 按行分割文本
        lines = input_text.split('\n')

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
        self.output_text.setPlainText('\n'.join(output_lines))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hex_converter = HexConverterWindow()
    hex_converter.show()
    sys.exit(app.exec_())