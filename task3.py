# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

input_list = [1, 4, 3, 8, 6, 1, 2, 4, 6, 9, 8, 8, 5, 2, 6, 5, 5, 5, 6, 3, 7, 0, 9, 3, 5, 6, 2, 3, 8, 0, 6, 8]
output_list = []
for i in range(0, len(input_list)):
    if input_list[i] not in output_list:
        output_list.append(input_list[i])
print('Исходная последовательность: ', input_list)
print('Неповторяющиеся элементы: ', output_list)