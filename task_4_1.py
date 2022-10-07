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

from decimal import Decimal

number = input(str('Вводим число: '))
raz = input(str('Вводим разрядность в формате "1.0000": '))
number=Decimal(number)
number = number.quantize(Decimal(raz))
print(number)
