# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000
#
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
#
# out
# # 8.988
# from decimal import Decimal, getcontext
# # num = input('Вводим число: ')
# # d = input('Вводим разрядность: ')
# getcontext().prec = 3
# print(Decimal(9**0.3))
#
# from decimal import Decimal
#
# p = input('Вводим число: ')
# raz = str(input('Вводим разрядность  в форме "0.0001":'))
# raz = raz[::-1][:-2]
# raz.replace('1', '1.')
# print(f'raz = {raz}')
# a = Decimal(p)
# a = a.quantize(Decimal(raz))
# print(a)

from decimal import *

num = float(input('Введите число '))
raz = input('Введите разрядность: ')
raz = int(len(raz.partition('.')[2]))
print(raz)
getcontext().prec = raz + 1
d = Decimal(num) / Decimal(1)
print(d)
