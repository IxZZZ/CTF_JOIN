# offset = 0x000055555575BAC0
# str = '84721'
# # str = '1584'
# for i in range(len(str)):
#     ida_bytes.patch_byte(offset+i, ord(str[i]))
adds = [0x140, 0x225, 0x299, 0x359, 0x689, 0x400, 0x500, 0x491]
strs = []
offset = 0x0000555555756020
for add in adds:
    str = ''
    for i in range(100):
        b = ida_bytes.get_bytes(offset+add+i,1)
        str += chr(int.from_bytes(b,byteorder='little'))
    strs.append(str)
print(strs)
