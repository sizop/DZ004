# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
#
# in
# 54
#
# out
# [2, 3, 3, 3]
#
# in
# 9990
#
# out
# [2, 3, 3, 3, 5, 37]
#
# in
# 650
#
# out
# [2, 5, 5, 13]

def s_num(num):  # простые числа в диапазоне до ...

    simple_number = []
    for j in range(2, num):
        count = 0
        for i in range(2, j):
            if j % i == 0:
                count += 1
        if count == 0:
            simple_number.append(j)
    return simple_number
    print(simple_number)


def division(number):
    simple_num = s_num(number)
    div_num = []
    for i in range(len(simple_num)):
        if number % simple_num[i] == 0:
            div_num.append(simple_num[i])
    return div_num

print(division(int(input('Вводим число:'))))
