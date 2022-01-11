# offset = 0x0000017A6132BEF0

# arr = []
# for i in range(32):
#     b = ida_bytes.get_bytes(offset+i*4,4)
#     arr.append(int.from_bytes(b,byteorder='little'))

# for i in arr:
#     print(hex(i),end=',')


import string


def cal_subStr(str, arr):
    s1 = 0
    for i in str[:4]:
        s1 += ord(i)
    print(s1, end='-')
    s2 = 0
    for i in str[4:]:
        s2 += ord(i)
    print(s2, end=' ')
    for k in range(len(arr)-1):
        if (s1-arr[k]) % 47 == 0:
            # print('here')
            if(s2-arr[k+1]) % 47 == 0:
                print('ok',arr[k],arr[k+1],end='')
    print()


def recal_number(n, i):
    while True:
        if n > 256+i*i:
            break
        n += 47

    return n-256-i*i


arr = [0x104, 0x104, 0x14e, 0x15f, 0x183, 0x154, 0x123, 0x17f, 0x192, 0x1a6, 0x177, 0x1c5, 0x188, 0x15d, 0x1c3, 0x194,
       0x198, 0x108, 0x12d, 0x1bb, 0x15d, 0x170, 0x179, 0x170, 0x15b, 0x184, 0x13f, 0x188, 0x169, 0x146, 0x13a, 0x17a]
str = 'FGMc0hqMoexNWthVyhRxpNSwbGLlUkkD'
str = 'LEgfcbFmrGnEoSbvwrUOMqinMhpUSmMe'

str_1 = '0123456789'

str_3 = 'HIJKLMNOPQRSTUVWXYZ'

str_4 = 'abcdefghijklmnopqrstuvwxyz'


str_2 = 'ABCDEFG'
arr_prev = []
for i in range(len(str)):
    n = str[i]
    if n in (str_1+str_3+str_4):
        arr_prev.append(recal_number(ord(n), i))
    else:
        arr_prev.append(recal_number(ord(n)-24, i))

print(arr_prev)


arr_prev_1 = []

for i in arr_prev:
    while True:
        if chr(int(i/4)) in (str_2+str_3+str_4):
            break
        i += 47
    arr_prev_1.append(i)

print(arr_prev_1)

arr_prev_2 = []
for i in arr_prev_1:
    mod = i % 4
    k = int(i/4)
    arr_prev_2.append(k)
    arr_prev_2.append(k)
    arr_prev_2.append(k)
    arr_prev_2.append(k+mod)


# offset = 0x0000016125BA1940
# for i in range(len(arr_prev_2)):
#     #print(chr(i),end='')
#     ida_bytes.patch_byte(offset+i,arr_prev_2[i])

total_str = str_1+str_2+str_3+str_4

prev_str = ''
for i in arr_prev_2:
    prev_str += chr(i)

print(prev_str)


for n in total_str:
    str_temp = ''
    sum_res = ord(n)
    for i in range(10):
        c = ord(prev_str[i])
        k = i
        if(i >= 9):
            if k == 9:
                continue
            k -= 1
        cal = c*sum_res*(k+1)+256
        while True:
            if cal <= 255:
                if chr(cal) in (str_1 + str_2+str_3+str_4):
                    break
            if cal >= 48:
                cal -= 47
            else:
                cal += 24
        str_temp += chr(cal)
    print(str_temp, end=' ')
    cal_subStr(str_temp, arr_prev_1)
    # if (str_temp in prev_str):
    #     print(n)
