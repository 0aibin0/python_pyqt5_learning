from PIL import Image


def convert_png_to_ico(png_path, ico_path):
    # 打开 PNG 图像文件
    png_image = Image.open(png_path)

    # 将 PNG 图像保存为 ICO 格式
    png_image.save(ico_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])

    print("转换完成")


if __name__ == "__main__":
    # 设置 PNG 输入和 ICO 输出路径
    png_file = "input.png"
    ico_file = "output.ico"

    # 调用转换函数
    convert_png_to_ico(png_file, ico_file)
