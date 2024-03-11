from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


class HexConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('dcs-generate-initcode')
        self.setGeometry(300, 300, 600, 400)

        # 创建分割器并设置为水平方向
        self.splitter = QSplitter(Qt.Horizontal)

        self.input_text = QTextEdit(self)
        self.input_text.setPlaceholderText("Enter hex strings (e.g., 1A,2B,3C,4D)")

        self.convert_button = QPushButton("Convert", self)
        self.convert_button.clicked.connect(self.convert_hex)

        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText("generate initcode \n(e.g. 0x39,0x00,0x00,0x04,0x1a,0x2b,0x3c,0x4d,)")

        self.splitter.addWidget(self.input_text)
        self.splitter.addWidget(self.output_text)

        layout = QVBoxLayout()
        layout.addWidget(self.splitter)
        layout.addWidget(self.convert_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.splitter.setSizes([self.size().width() // 2, self.size().width() // 2])

    def convert_hex(self):
        input_str = self.input_text.toPlainText()

        # 判断输入字符是否包含"REGISTER"，如果有，则提前删除
        if "REGISTER" in input_str:
            input_str = input_str.replace("REGISTER", "")

        # 按行分隔输入字符串
        rows = input_str.split('\n')
        output_rows = []
        for row in rows:

            # 删除该行中第一个出现的'//'及其之后的所有内容
            if '//' in row:
                row = row[:row.find('//')]

            # 跳过空行
            if not row.strip():  # 如果row是一个空行或者只包含空白字符，那么row.strip()将返回一个空字符串（即False）
                continue

            # 按列分隔每行
            hex_numbers = row.split(',')
            hex_numbers = [num.strip() for num in hex_numbers]  # 去除每个元素的首尾空白

            # 检查倒数第二个值是否等于'01'，如果是则删除它
            if len(hex_numbers) > 1 and hex_numbers[-2].strip() == '01':
                hex_numbers.pop(-2)  # 删除倒数第二个元素

            # 检查倒数第四个值是否等于'03'，如果是则删除它
            if len(hex_numbers) > 3 and hex_numbers[-4].strip() == '03':
                hex_numbers.pop(-4)  # 删除倒数第二个元素

            hex_count = len([number for number in hex_numbers if number.strip()])
            hex_count_hex = '0x{:02x}'.format(hex_count)  # 转换为两位十六进制数，并添加0x前缀

            # 根据hex_count_hex的值添加不同的前缀
            if hex_count_hex == '0x01':
                prefix = '0x05,0x00,0x00'
            elif hex_count_hex == '0x02':
                prefix = '0x15,0x00,0x00'
            else:
                prefix = '0x39,0x00,0x00'

            # 在每一行的开始添加前缀和hex_count_hex
            output_row = [prefix, hex_count_hex] + ['0x' + number.strip() for number in hex_numbers if number.strip()]

            # 在最后一个元素后也加上逗号，通过添加一个空字符串到列表实现
            output_row.append('')

            # 用逗号连接输出行的元素，包括最后的空字符串
            output_row_str = ','.join(output_row)
            output_rows.append(output_row_str)

            # 输出为新的格式，每行以特定前缀和hex_count_hex开头，接着是原始十六进制数，每个元素用逗号隔开，且行尾也有逗号
        output_str = '\n'.join(output_rows).lower()
        self.output_text.setPlainText(output_str)


def main():
    app = QApplication([])
    window = HexConverterWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
