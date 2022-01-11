# offset = 0x61FA80

# str  = 'ab53f132c859a706'
# for i in range(len(str)):
#     ida_bytes.patch_byte(offset+2*i,ord(str[i]))


offset = 0x00000000061F9E0
str = b''
for i in range(191):
    str += ida_bytes.get_bytes(offset+i,1)

file = open('payload.txt','wb')

print(str)
file.write(str)

file.close()

print(str[0],str[1],str[2])