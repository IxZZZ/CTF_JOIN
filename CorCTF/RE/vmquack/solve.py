def padding(str):
    if len(str)%2 !=0:
        str = '0'+ str
    return str


#offset = 0x4B15B0 # duck data
offset = 0x4B14F0


xor_8_bytes = int.from_bytes(
    ida_bytes.get_bytes(offset, 8), byteorder='little')

len_str = int.from_bytes(ida_bytes.get_bytes(offset+8, 2), byteorder='little')
next_offset = int.from_bytes(ida_bytes.get_bytes(offset+16,4),byteorder='little')
str = b''
for i in range(0,len_str,8):
    bytes_8 = int.from_bytes(ida_bytes.get_bytes(next_offset+i,8),byteorder='little')
    str += bytes.fromhex(padding(hex(xor_8_bytes^bytes_8)[2:]))[::-1]

print(str)
    

