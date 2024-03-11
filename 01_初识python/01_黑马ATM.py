money = 100
Flag = True


name = input("请输入您的名字")


def find_money(show_header):
    """
    查询当前余额
    :return:
    """
    global money
    if show_header:
        print("--------------------查询余额----------------------")
    print(f"{name},您好，您的余额剩余:{money}元")


def add_money(data):
    """
    存款函数
    :param data:
    :return:
    """
    global money
    money += data
    print("--------------------存款----------------------")
    print(f"{name},您好，您存款:{data}元成功")
    find_money(False)


def del_money(data):
    """
    取款函数
    :param data:
    :return:
    """
    global money
    if money < data:
        print("余额不足，无法取款")
    else:
        money -= data
        print("--------------------取款----------------------")
        print(f"{name},您好，您取款:{data}元成功")
        find_money(False)


def main():
    """
    主菜单函数
    :return:
    """
    print("--------------------主菜单----------------------")
    print(f"{name},您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额\t\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")

    return input("请输入您的选择")


while Flag:
    keyboard_input = main()
    if keyboard_input == "1":
        find_money(True)
        continue
    elif keyboard_input == "2":
        num = int(input("您想要存款的金额是:"))
        add_money(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取款的金额是:"))
        del_money(num)
        continue
    else:
        print("程序退出啦")
        Flag = False
