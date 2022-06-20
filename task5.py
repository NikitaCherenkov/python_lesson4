# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def read_file(file_name):
    f = open(file_name)
    lines = []
    lines += f.readlines()
    return lines[0]

file0_name = input('Введите название первого файла: ')
file1_name = input('Введите название второго файла: ')
file_output_name = input('Введите название файла с суммой многочленов, который будет создан: ')
min = read_file(file0_name).split(' + ')
max = read_file(file1_name).split(' + ')
if len(min) > len(max):
    temp = min
    min = max
    max = temp
file_output = ''
temp = 0
while not (len(max) == len(min)):
    file_output += max[temp] + ' + '
    max.pop(0)
for i in range(0, len(max)):
    for j in range(0, len(min)):
        if max[i].__contains__('x^') and min[j].__contains__('x^'):
            if int(max[i].split('x^')[1]) > int(min[j].split('x^')[1]):
                file_output += max[i] + ' + '
                break
            if int(max[i].split('x^')[1]) == int(min[j].split('x^')[1]):
                file_output += str(int(max[i].split('x^')[0]) + int(min[j].split('x^')[0])) + 'x^' + str(i + 1) + ' + '
                break
        if max[i].__contains__('x') and min[j].__contains__('x') and not max[i].__contains__('^') and not min[j].__contains__('^'):
            file_output += str(int(max[i].split('x')[0]) + int(min[j].split('x')[0])) + 'x + '
            break
        if max[i].__contains__('=') and min[j].__contains__('='):
            file_output += str(int(max[i].split(' = ')[0]) + int(min[j].split(' = ')[0])) + ' = 0'
            break
print(file_output)