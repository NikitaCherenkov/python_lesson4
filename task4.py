# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0

import random

name = str(input('Введите название файла: '))
file = open(name, 'w')
rate = int(input('Введите натуральную степень n: '))
form = ''
for i in range(0, rate):
    if not i == rate - 1:
        form += str(random.randint(0, 100)) + 'x^' + str((rate - i)) + ' + '
    else:
        form += str(random.randint(0, 100)) + 'x + ' + str(random.randint(0, 100)) + ' = 0'
file.write(form + '\n')
