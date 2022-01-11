file = open('prog.bin','rb')

str_bytes = file.read()

arr = []
for i in str_bytes:
    arr.append(i%8)

print(arr[:0x17+100])