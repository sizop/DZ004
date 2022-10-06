# 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
#
# in
# "poly.txt"
# "poly_2.txt"
#
# out
# The contents of the files do not match!

def w_r(n):
    # for i in range(n):
    with open('out_1.txt', 'r') as my_f_1:
        line_1 = my_f_1.readline()[:-4]
    with open('out_2.txt', 'r') as my_f_2:
        line_2 = my_f_2.readline()
    return (f'{line_1}+ {line_2}')


with open('out_3.txt', 'w') as my_f_3:
    for i in range(int(3)):
        print(w_r(i))
        my_f_3.write(w_r(i))