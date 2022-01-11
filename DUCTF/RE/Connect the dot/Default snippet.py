offset = 0x0000000000004080

arr = []

for i in range(3600):
    b = ida_bytes.get_bytes(offset+i*4, 4)
    arr.append(int.from_bytes(b, byteorder='little'))
arr_maze = []
for i in range(60):
    arr_maze.append(arr[i*60:i*60+60])

print(arr_maze)
offset = 0x0000000000004060

arr = []

for i in range(8):
    b = ida_bytes.get_bytes(offset+i*4, 4)
    arr.append(int.from_bytes(b, byteorder='little'))

print(arr)
