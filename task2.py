# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите натуральное число N: '))
multipliers_list = []
stop = False
while not stop:
    for i in range(2, 10):
        if N % i == 0:
            N = N / i
            multipliers_list.append(i)
            break
        if i >= 9:
            if len(multipliers_list) == 0 or N > 9:
                multipliers_list.append(int(N))
            stop = True
print(multipliers_list)
