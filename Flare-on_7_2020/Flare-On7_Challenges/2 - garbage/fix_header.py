f = open('garbage.exe', 'rb')
data = f.read()
current_size = len(data)

padding_size = 0x1929c + 0x10 - 0x19124
final_size = padding_size + current_size

align = 0x200 - (final_size % 0x200)
f_w = open('fix_header.exe', 'wb')
data += b'\x00'*(align+final_size-current_size) 
f_w.write(data)
f_w.close()
f.close()
