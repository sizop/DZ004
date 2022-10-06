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
# d = float(input())
# getcontext().prec = 10
# print(1*(Decimal(d)))
# print(Decimal(9).quantize(Decimal(10)))
p = input()
raz=str(input('Вводим разрядность:'))
raz=raz[::-1][:-2]
raz.replace('1', '1.')
# raz=raz[:-2]
print(raz)
a = Decimal(p)
a = a.quantize(Decimal('1.0000'))#raz))
print(a)
