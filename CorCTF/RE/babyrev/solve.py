from z3 import *
from math import *


def is_prime(x):
    if x<2:
        return 0
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return 0
    return 1


def rotate(x, n):
    ascii_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lower = 'abcdefghijklmnopqrstuvwxyz'
    if chr(x).isupper():
        return ord(ascii_upper[(x-n-65) % 26])
    elif chr(x).islower():
        return ord(ascii_lower[(x-n-97) % 26])
    else:
        return x


arr = []
for i in range(0x14):
    v6 = 4*i
    while is_prime(v6) != 1:
        v6 += 1
    arr.append(v6)

arr_check = [117, 106, 112, 63, 95, 111, 72, 121, 95,
             108, 120, 105, 117, 95, 122, 120, 95, 117, 118, 101]

flag = ''
for i in range(len(arr_check)):
    flag += chr(rotate(arr_check[i],arr[i]))

print('corctf{'+flag+'}')
