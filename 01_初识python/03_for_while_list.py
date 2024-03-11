my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while_list = []
for_list = []


def while_func():
    index = 0
    while index < len(my_list):
        element = my_list[index]
        if element % 2 == 0:
            while_list.append(element)
        index += 1
    print(while_list)


def for_func():
    for element in my_list:
        if element % 2 == 0:
            for_list.append(element)
    print(for_list)


while_func()
for_func()