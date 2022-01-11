
# the read section flag
# offset = 0x00007FFCF3552170
# str = 'cbbefea802bf596615e073d3419262f0'
# for i in range(int(len(str)/2)):
#     # ida_bytes.patch_byte(offset+i, ord(str[i]))
#     ida_bytes.patch_byte(offset+i, int(str[2*i]+str[2*i+1], 16))
#     # print(int(str[2*i]+str[2*i+1],16))


# the blue section flag

str = 'cat flag2.txt'

offset = 0x00007FFD103A8030
for i in range(len(str)):
    ida_bytes.patch_byte(offset+i,ord(str[i]))
