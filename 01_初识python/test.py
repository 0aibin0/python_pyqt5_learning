# message = "hello python world!!!"
# print(message)
# message = "aibin"
# print(message)
# print("---------------")
# print(message.lower())
# print("---------------")
# print(message.upper())
# print("---------------")
# print(message.title())
#
#
# first_name = "yin"
# second_name = "xuebin"
# full_name = first_name + second_name
#
# print(full_name)
# print("\tyin\n \txue\n \tbin\n")
#
# money = 100
# print("今天还剩", money, "元")
#
#
# type_name = type(money)
# print(type(money))
# print(type(12.12))
# print(type("work"))
# print(type_name)
#
#
# name = "尹雪斌"
# address = "南京"
# print("我是： ", name, " 地址是：", address)
#
#
# class_num = 23
# money = 12445
# message = "班级:%d的平均工资是%s" % (class_num, money)
# print(message)
#
#
# name = "传智播客"
# stock_price = 19.99
# stock_code = "003032"
# stock_price_daily_growth_factor = 1.2
# growth_days = 7
# finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
#
# print(f"公司：{name}, 股票代码：{stock_code}, 当前股价：{stock_price}")
# print("每日增长系数是：%.2f, 经过%d天的增长后, 股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days, finally_stock_price))

# name = input("请告诉我你是谁\n")
# print("我知道了，你是%s" % name)
# user_name = input("请输入您的名称")
# user_type = input("请输入您的等级")
# print(f"您好：{user_name},您是尊贵的{user_type} 用户，欢迎您的光临！")


# age = int(input("请输入您的年龄："))
#
# if age >= 18:
#     print("你已经成年了\n")
# else:
#     print("你现在还未成年\n")
#
# print("时间过得真快！！！")


# 三次机会猜数字
# import random
# num = random.randint(1,10)
# print("欢迎来到益智游戏练习！")
# guess_num = int(input("请你来猜猜看吧！"))
#
# if guess_num == num:
#     print("恭喜你，第一次就猜中了")
# else:
#     if guess_num > num:
#         print("您猜测的数字大了")
#     else:
#         print("您猜测的数字小了")
#     guess_num = int(input("请再次输入您的数字"))
#     if guess_num == num:
#         print("恭喜你，猜中了")
#     else:
#         if guess_num > num:
#             print("您猜测的数字大了")
#         else:
#             print("您猜测的数字小了")
#         guess_num = int(input("请第三次输入您的数字"))
#         if guess_num == num:
#             print("恭喜你，猜中了")
#         else:
#             if guess_num > num:
#                 print("您猜测的数字大了")
#             else:
#                 print("您猜测的数字小了")


# 无限次数猜数字小游戏
# import random
# num = random.randint(1,100)
# guess_time = 0
# while True:
#     guess_num = int(input("请输入您猜测的数字"))
#     guess_time += 1
#     if guess_num == num:
#         print("恭喜您，猜对了")
#         print(f"您猜测的次数为{guess_time}")
#         break
#     elif guess_num > num:
#         print("您猜测的数字大了")
#     else:
#         print("您猜测的数字小了")


# while实现1-100的累加和
# i = 1
# num1 = 0
# while i <= 100:
#     num1 = num1 + i
#     i += 1
# print(f"和是{num1}")


# 九九乘法表
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i}={i*j}\t", end='')
#         j = j + 1
#     i += 1
#     print()
#

# for 循环使用示例
# name = "yinxuebin"
# for x in name:
#     if x == "x":
#         print("遇到了x")
#     print(f"{x}")

# name = "itheima is a brand of itcast"
# count = 0
# for x in name:
#     if x == "a":
#         count += 1
# print(f"{name}中共有{count}个a")

# for x in range(10):
#     print(x)
#
# for x in range(1,5):
#     print(x)
#
# for x in range(1,10,3):
#     print(x)

# count = 0
# for x in range(1,100):
#     if x % 2 == 0:
#         count += 1
# print(count)

# for循环九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {j * i}\t", end='')
#     print()


# 发工资示例
# money = 10000
# for i in range(1, 21):
#     import random
#     num = random.randint(1, 10)
#
#     if num < 5:
#         print(f"员工{i},绩效分{num},低于5，不发工资，下一位")
#         continue
#     if money >= 1000:
#         money -= 1000
#         print(f"向员工{i}发放工资1000元，账户余额还剩{money}元")
#     else:
#         print("工资发完啦，下个月领取吧")
#         break


# name_1 = "asdfgv"
# name_2 = "fdfe"
# name_3 = "adfafagawgf"
#
#
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     return count
#
#
# lengh_1 = my_len(name_1)
# print(lengh_1)
# lengh_2 = my_len(name_2)
# print(lengh_2)
# lengh_3 = my_len(name_3)
# print(lengh_3)


favorite_language = {
    'jen': ['python', 'ruby'],
    'sarch': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_language.items():
    # 获取字典中的键值。name保存键，language保存值
    print(f"{name}'s favorite language are:")
    print(f"language 是{languages}")
    for language in languages:
        print(f"语言是{language}")
