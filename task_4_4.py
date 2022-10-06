# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10)
# многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
#
# in
# 0
# -1
# 4
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0
from random import randint

signs = ['+', '-']

with open("out.txt", "a+", encoding="utf-8") as my_f:
    for j in range(0, 3):
        formula = []
        num = int(input('Введите число:'))
        if num == 0:
            continue
        i = 9
        while i > 1:
            if i == 7:
                i-=1
                continue
            formula += (randint(1, num)), ('*x^'), (i)
            i -= 1
            if i == 1:
                continue
            formula += (' ', signs[randint(0, 1)], ' ')
        formula += (' = 0')
        j += 1

        convert = ''.join(map(str, formula))
        my_f.write(f'{convert}\n')
        print(f'{convert}\n')


