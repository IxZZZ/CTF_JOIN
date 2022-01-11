# offset = 0x7198B0

# arr = []
# arr_get = []

# # b = ida_bytes.get_bytes(offset, 4)
# off = 0x00713E68
# for i in range(0, 255):

#     b = ida_bytes.get_bytes(off+i*2, 2)
#     b_i = int.from_bytes(b, byteorder='little')
#     arr_get.append(b_i)
#     if (b_i & 8) & 0xffff != 0:
#         arr.append(i)
# print(arr_get)
# print(arr)

arr = [44, 98, 46, 120, 62, 74, 21, 1, 31, 110, 0, 84, 50, 69, 93,
        110, 10, 84, 25, 110, 25, 89, 8, 110, 11, 93, 12, 86, 16, 49]

# for i in range(30):
#     b = ida_bytes.get_bytes(offset+i*1, 1)
#     b_i = int.from_bytes(b, byteorder='little')
#     arr.append(b_i)

print(arr)

key_1 = 109
key_2 = 49

for i in range(len(arr)):
    if i %2 == 0:
        print(chr(key_1^arr[i]),end='')
    else:
        print(chr(key_2 ^ arr[i]), end='')
