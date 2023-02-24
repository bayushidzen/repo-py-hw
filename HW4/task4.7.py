# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def read_file(name):
    f = open(name,'r')
    for line in f:
        name = line
    f.close()
    return name

def rep_data1(text):
    text = text.replace(' = 0 ', '')
    return text

def split_data(text):
    text = text.split(' + ')
    for i in range(0, len(text)):
        text[i] = text[i].split('*x^')
    return text

def str_to_int(text):
    for i in range(0, len(text)):
        for j in range(0, len(text[i])):
            text[i][j] = int(text[i][j])
    return text

def polynomial_sum(arr1, arr2):
    sum_arr = []
    x_arr = []
    result_arr = [[],[]]
    for i in range(0, len(arr1)):
        x_arr.append(arr1[i][1])
        sum_arr = (arr1[i][0]+arr2[i][0])
        result_arr[0].append(sum_arr)
        result_arr[1].append(x_arr[i])
    return result_arr

def make_equation():
    equality = ""
    for i in range(0, len(file1)-1):
        equality += f'{arr_sum[0][i]}' + '*x^'+ f'{arr_sum[1][i]}'+ ' + '
    equality += f'{arr_sum[0][-1]}' + '*x^'+ f'{arr_sum[1][-1]}'+' = 0'
    return equality

def make_file_great_again(t):
    f = open('new_test.txt','w')
    f.write(t)
    print(t)
    
file1 = 'test1.txt'
file1 = str_to_int(split_data(rep_data1(read_file(file1))))
print(file1)

file2 = 'test2.txt'
file2 = str_to_int(split_data(rep_data1(read_file(file2))))
print(file2)
arr_sum = polynomial_sum(file1, file2)
print(arr_sum)

make_file_great_again(make_equation())