# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def read_file(file_name):
    f = open(file_name)
    lines = []
    lines += f.readlines()
    return lines[0]

file0_name = input('Введите название первого файла: ')
file1_name = input('Введите название второго файла: ')
min = read_file(file0_name).split(' + ')
max = read_file(file1_name).split(' + ')
if len(min) > len(max):
    temp = min
    min = max
    max = temp
file_output = ''
while not (len(max) == len(min)):
    file_output += max[0] + ' + '
    max.pop(0)
if max[0].__contains__('x^'):
    temp1 = int(max[0].split('x^')[1])
    for i in range(0, temp1 - 1):
        file_output += str(int(max[0].split('x^')[0]) + int(min[0].split('x^')[0])) + 'x^' + str(len(max) - 1) + ' + '
        max.pop(0)
        min.pop(0)
if max[0].__contains__('x'):
    file_output += str(int(max[0].split('x')[0]) + int(min[0].split('x')[0])) + 'x + '
    max.pop(0)
    min.pop(0)
file_output += str(int(max[0].split(' = ')[0]) + int(min[0].split(' = ')[0])) + ' = 0'
file_output_name = input('Введите название файла с суммой многочленов, который будет создан: ')
file = open(file_output_name, 'w')
file.write(file_output + '\n')
