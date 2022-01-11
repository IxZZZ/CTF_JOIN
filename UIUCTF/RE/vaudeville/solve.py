import struct
from pwn import *

def caculate_len_arr_str():
    start_offset = 0x000055DFE84FB020
    # end_offset = 0x000055DFE84FB818

    # print('number of str ref: ', (start_offset-end_offset)/8)
    # arr_str_len = []
    # while start_offset != end_offset+8:
    #     str = read_str(start_offset, 0)
    #     arr_str_len.append(len(str))
    #     start_offset += 8

    # print(arr_str_len)


def read_str(offset, multi):

    bytes = ida_bytes.get_bytes(offset + multi*8, 8)

    new_offset = struct.unpack('<Q', bytes)[0]

    str = ''
    while True:

        bytes = ida_bytes.get_bytes(new_offset, 1)

        bytes = int.from_bytes(bytes, 'little')

        if bytes == 0:
            break

        new_offset += 1
        str += chr(bytes)
    return str


def generate_arr(number):
    arr = []
    for i in range(32):
        arr.append(0x30)
    for i in range(32):
        arr.append(((number & (1 << i)) != 0)+48)
        # print(chr(((number & (1 << i)) != 0)+48), end='')
    for i in range(32):
        arr.append(0x30)
    print()
    return arr


def calculate_res(arr):
    res = 0
    for i in range(len(arr)):
        res += (arr[i] & 1) << i

    return res >> 32


def print_arr(arr):
    for i in arr:
        print(hex(i & 1), end=' ')

    print()


def get_len_str(arr_str_len, arr, index_1, index_2):
    return arr_str_len[arr[index_1]]+arr_str_len[arr[index_2]]


arr_str_len = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136,
               137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]

# p = remote('vaudeville.chal.uiuc.tf', 1337)


# p = process('./vaudeville')
# p.recvuntil('Challenge:')

# number = p.recvline().strip()


# number = int(number, 10)

# print('random number: ',number)
number = 1719236712
arr = generate_arr(number)

offset = 0

for _ in range(140):
    index_19 = 19
    index_32 = 32
    new_arr = []
    for i in range(32):
        # str = read_str(offset, arr[index_32+i])
        # str += read_str(offset, arr[index_19+i])
        new_arr.append(get_len_str(arr_str_len, arr,
                       index_32+i, index_19+i) & 0xff)

    arr = arr[:32] + new_arr + arr[64:]

    # print_arr(new_arr)

    index_32 = 32
    index_49 = 49

    new_arr = []

    for i in range(32):
        # str = read_str(offset, arr[index_32+i])
        # str += read_str(offset, arr[index_49+i])
        new_arr.append(get_len_str(
            arr_str_len, arr, index_32+i, index_49+i) & 0xff)
        # print(str,'-',len(str))

    arr = arr[:32] + new_arr + arr[64:]

    # print_arr(new_arr)
    # print(len(arr))

    index_32 = 32
    index_27 = 27

    new_arr = []

    for i in range(32):
        # str = read_str(offset, arr[index_32+i])
        # str += read_str(offset, arr[index_27+i])
        new_arr.append(get_len_str(
            arr_str_len, arr, index_32+i, index_27+i) & 0xff)
        # print(str,'-',len(str))

    arr = arr[:32] + new_arr + arr[64:]

    # print_arr(new_arr)
    # print(len(arr))


# print_arr(arr)
# print(len(arr))

sum = calculate_res(arr)
print(hex(sum))
# print(hex(sum))
sum_str = bin(sum)[2:][::-1]
# print(sum_str[::-1])
elements = list(sum_str)


arr_back_ward = []
for i in elements:
    arr_back_ward.append(ord(i)-48)
# print_arr(arr_back_ward)
print()

for _ in range(7):
    arr_res = list('0'*32*3)

    index_32 = 32
    index_27 = 27

    for i in range(len(arr_back_ward)):
        if arr_back_ward[i] == 0:
            if arr_res[index_27+i] == '0':
                arr_res[index_27+i] = 0
                arr_res[index_32+i] = 0
            else:
                arr_res[index_32+i] = arr_res[index_27+i]
        else:
            if arr_res[index_27+i] == '0':
                arr_res[index_27+i] = 0
                arr_res[index_32+i] = 1
            else:
                arr_res[index_32+i] = 1 - int(arr_res[index_27+i])

    # print_arr(arr_res[32:64])
    # print_arr(arr_res[27:27+32])
    #print()

    index_32 = 32
    index_27 = 49

    arr_back_ward = arr_res[32:64]

    arr_res = list('0'*32*3)
    for i in range(0, 32):
        arr_res[i] = 0
    for i in range(64, 96):
        arr_res[i] = 0

    for i in range(31, -1, -1):
        if arr_back_ward[i] == 0:
            if arr_res[index_27+i] == '0':
                arr_res[index_27+i] = 0
                arr_res[index_32+i] = 0
            else:
                arr_res[index_32+i] = arr_res[index_27+i]
        else:
            if arr_res[index_27+i] == '0':
                arr_res[index_27+i] = 0
                arr_res[index_32+i] = 1
            else:
                arr_res[index_32+i] = 1 - int(arr_res[index_27+i])

    arr_back_ward = arr_res[32:64]

    # print_arr(arr_res[32:64])
    # print_arr(arr_res[49:49+32])

    #print()

    arr_res = list('a'*32*3)

    index_32 = 32
    index_27 = 19

    for i in range(len(arr_back_ward)):
        if arr_back_ward[i] == 0:
            if arr_res[index_27+i] == 'a':
                arr_res[index_27+i] = 0
                arr_res[index_32+i] = 0
            else:
                arr_res[index_32+i] = arr_res[index_27+i]
        else:
            if arr_res[index_27+i] == 'a':
                arr_res[index_27+i] = 0
                arr_res[index_32+i] = 1
            else:
                arr_res[index_32+i] = 1 - int(arr_res[index_27+i])
    # print_arr(arr_res[32:64])
    # print_arr(arr_res[19:19+32])

    # print()
    res = ''.join([str(i) for i in arr_res[32:64]])
    # print(res)
    if (_ == 6):
        final = int(res[::-1], 2)
        print('final: ',final)
        # p.recvuntil('Response:')
        # p.sendline(p64(final))
    arr_back_ward = arr_res[32:64]

# p.interactive()
