
from os import error



def operator(a, b, operator):
    if operator == 'add':
        return a+b
    elif operator == 'multiply':
        return a*b
    elif operator == 'divide_before_after':
        return int(a/b)
    elif operator == 'subtrac_before_after':
        return a-b
    else:
        print('error')


def caculate(index, const_1, const_2):
    v5 = index % const_2
    v6 = 1
    while const_1:
        if (const_1 & 1) != 0:
            v6 = v5*v6 % const_2
        v5 = v5*v5 % const_2
        const_1 >>= 1

    return v6


def check(arr):
    res = 0
    for i in range(0, 33, 1):
        v2 = operator(arr[2*i], arr[2*i+1], arr_func_1[i])&0xffffffff
        #print(v2,end='')
        v0 = caculate(i, 0x35, 0x383)
        if v2 != caculate(v0, 0x43, 0x383):
            res = 1
    return res


def swap(arr, i, j):
    a = arr[i]
    arr[i] = arr[j]
    arr[j] = a
    return arr




def swap_fuc_and_value(arr_1, arr_2, arr_func_1, arr_func_2, rand,k):
    for i in range(33):
        #print(int(rand[k], 10))
        arr_1 = swap(arr_1, 2*i, int(rand[k], 10)*2)
        arr_1 = swap(arr_1, 2*i+1, int(rand[k], 10)*2+1)
        #print(arr_1)
        arr_2 = swap(arr_2, 2*i, int(rand[k], 10)*2)
        arr_2 = swap(arr_2, 2*i+1, int(rand[k], 10)*2+1)
        arr_func_1 = swap(arr_func_1, i, int(rand[k], 10))
        #print(arr_func_1)
        arr_func_2 = swap(arr_func_2, i, int(rand[k], 10))
        k += 1

    return (arr_1, arr_2, arr_func_1, arr_func_2,k)


def final_print():
    str = ''
    for i in range(0, 33, 1):
        v0 = operator(arr_2[2*i], arr_2[2*i+1], arr_func_2[i])
        str += chr(v0)
    # if str[:5] == 'IJCTF':
    #     print(str)

file = open('text.txt', 'r')
arr_1 = [0x4b8a7deb]
str = file.read()
for i in str.split(','):
    arr_1.append(int(i, 16))
file.close()
file = open('text2.txt', 'r')
arr_2 = [0x00330]
str = file.read()
for i in str.split(','):
    arr_2.append(int(i, 16))
arr_func_1 = ['multiply', 'add', 'add', 'multiply', 'divide_before_after', 'subtrac_before_after', 'multiply', 'divide_before_after', 'divide_before_after', 'subtrac_before_after', 'add', 'divide_before_after', 'subtrac_before_after', 'add', 'subtrac_before_after', 'divide_before_after', 'subtrac_before_after',
              'multiply', 'divide_before_after', 'divide_before_after', 'divide_before_after', 'multiply', 'divide_before_after', 'multiply', 'subtrac_before_after', 'subtrac_before_after', 'add', 'multiply', 'add', 'subtrac_before_after', 'divide_before_after', 'subtrac_before_after', 'subtrac_before_after']
arr_func_2 = ['divide_before_after', 'divide_before_after', 'divide_before_after', 'add', 'subtrac_before_after', 'subtrac_before_after', 'divide_before_after', 'add', 'divide_before_after', 'divide_before_after', 'divide_before_after', 'divide_before_after', 'subtrac_before_after',
              'divide_before_after', 'subtrac_before_after', 'add', 'subtrac_before_after', 'add', 'divide_before_after', 'add', 'subtrac_before_after', 'divide_before_after', 'add', 'divide_before_after', 'add', 'divide_before_after', 'divide_before_after', 'add', 'add', 'add', 'add', 'subtrac_before_after', 'add']
file.close()
file = open('random.txt', 'r')
str = file.read()
randoms = str.split(',')
print('random len = ',len(randoms))
k = 0
n = 5
while check(arr_1):
    #print('.', end='')
    arr_1, arr_2, arr_func_1, arr_func_2,k = swap_fuc_and_value(
        arr_1, arr_2, arr_func_1, arr_func_2, randoms,k)
    # for i in arr_1:
    #     print(hex(i),end=' ')
    # for i in arr_1:
    #     print(hex(i), end=' ')
    
    # break

    # n -= 1
    # if n == 0:
    #     break

final_print()
print('done')

