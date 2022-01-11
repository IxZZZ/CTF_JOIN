# offset = 0x00005639E18A0020
# add = 0
# str =''
# for i in range(65,296):
#     str+=chr(int.from_bytes(ida_bytes.get_bytes(offset+add+i,1),byteorder='little'))

# print(str)

import string
str_arr = 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff30030587801234562301034123801234412115345567801232762751324567803356468145234567423634656801234567801234567801234567801234567801234567801234567801234567801234567801234567801234567801234567801248577878274567801215767600234567086284567'

dict_ascii = {}
for i in range(40, 126):
    index = int(str(i), 16)
    dict_ascii[chr(i)] = str_arr[index]

# print(dict_ascii)
dict_map = {0: 6, 8: 5, 16: 8, 24: 3, 31: 3, 1: 2, 9: 6, 17: 1, 25: 0, 2: 0, 10: 4, 18: 5, 26: 2, 32: 3, 3: 8, 11: 5, 19: 3,
            27: 7, 4: 3, 12: 8, 20: 3, 28: 8, 33: 3, 5: 6, 13: 5, 21: 5, 29: 6, 6: 1, 14: 0, 22: 4, 30: 2, 34: 5, 7: 5, 15: 3, 23: 1, 35: 8}

str_number_arr = ['1854']
dict_flag = {}
str_order = [7, 15, 23, 35]
for str_number in str_number_arr:
    for index in range(len(str_number)):
        for i, j in dict_ascii.items():
            if j == str_number[index] and ord(i) % 9 == dict_map[str_order[index]]:
                dict_flag[str_order[index]] = i


print(dict_flag)
