# Ввычислить число пи, (использовать Ряд Нилаканта или любой другой вариант расчета числа Пи
# примеры расчетов можно посмотреть по ссылке ==> http://www.swsys.ru/files/2018-2/409-413.pdf ) c заданной точностью d

import math

d = float(input('Введите необходимую точность: '))
prec = 0
while d < 1:
    d *= 10
    prec += 1
calculated = 3
temp = 1
i = 2
while round(math.pi, prec) != round(calculated, prec):
    calculated = calculated + 4 * temp / (i * (i + 1) * (i + 2))
    i += 2
    temp = -temp
print(round(calculated, prec))