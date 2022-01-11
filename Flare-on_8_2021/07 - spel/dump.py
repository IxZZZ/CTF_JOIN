offset = 0x1800168F0
size = 0x17A00

file = open('file_dump', 'wb')
for i in range(size):
    b = ida_bytes.get_bytes(offset+i, 1)
    file.write(b)
file.close()
