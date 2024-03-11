

my_str = "itheima itcast boxuegu"

count = my_str.count("it")
print(f"字符串{my_str}中有：{count}个it字符")

replace_str = my_str.replace(" ", "|")
print(f"字符串{my_str}中,被替换空格后，结果：{replace_str}")

list = replace_str.split('|')
print(f"字符串{my_str}中,按照|分割后，得到：{list}")