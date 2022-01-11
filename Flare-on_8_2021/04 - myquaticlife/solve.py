# offset = 0x0019CF40

hash = '6c5215b12a10e936f8de1e42083ba184'


# for i in range(len(hash)):
#     ida_bytes.patch_byte(offset+i,ord(hash[i]))
# offset = 0x0019CF80


# arr_const = []

# for i in range(31):
#     b = ida_bytes.get_bytes(offset+i,1)
#     arr_const.append(int.from_bytes(b,byteorder='little'))

# print(arr_const)

arr_const = [150, 37, 164, 169, 163, 150, 154, 144, 159, 175, 229, 56, 249, 129,
             158, 22, 249, 203, 228, 164, 135, 143, 143, 186, 210, 157, 167, 209, 252, 163, 168]

print(arr_const[-14])
print(len(arr_const))
# jetsam = 'newauiSLdkvHwdwAZ'
# flotsam = 'DFWEyEWPXopvMBGgsuhn'

# for i in jetsam:
#     b = ord('o')+ord(i)
#     if chr(b^arr_const[-2]) in flotsam:
#         print(i)
