# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
#
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
#
# in
# -1
#
# out
# Negative value of the number of numbers!
# []
#
# in
# 10
#
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
import random


def cr_nln():
    while True:
        try:
            num = int(input('Введите размерность: '))
            if num > 0:
                list_num = [random.randint(-5, 5) for i in range(num)]
                return list_num
            return "Negative value of the number of numbers!"
        except ValueError:
            print('Это не число! Повторим: ')


list_num = (cr_nln())
list_out = []
for i in range(len(list_num)):
    if list_num.count(list_num[i]) == 1:
        list_out.append(list_num[i])
print(f'Исходные значения: {list_num}\nСписок неповторяющихся элементов: {list_out}')
