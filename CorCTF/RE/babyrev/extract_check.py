offset = 0x00005572D8C14010

arr = []
for i in range(0x14):
    b = ida_bytes.get_bytes(offset+i, 1)
    arr.append(int.from_bytes(b,byteorder='little'))

print(arr)
