import string
v33 = list('A'*37)
v33[0] = 0x98
v33[1] = 0x69
v33[2] = 152
v33[3] = 103
v33[4] = 158
v33[5] = 100
v33[6] = 159
v33[7] = 119
v33[8] = 173
v33[9] = 101
v33[10] = 118
v33[11] = 118
v33[12] = 178
v33[13] = 105
v33[14] = 158
v33[15] = 115
v33[16] = 169
v33[17] = 87
v33[18] = 180
v33[19] = 35
v33[20] = 158
v33[21] = 119
v33[22] = 179
v33[23] = 146
v33[24] = 169
v33[25] = 88
v33[26] = 174
v33[27] = 45
v33[28] = 89
v33[29] = 101
v33[30] = 168
v33[31] = 21
v33[32] = 89
v33[33] = 33
v33[34] = 173
v33[35] = 102
v33[36] = 165

print(v33)

#ascii = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm_{}'
ascii = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm_{}'
ascii = string.printable
for i in range(len(v33)):
    const1 = 0x13
    const2 = 0x37
    if i % 2 == 1:
        const1 = 0x37
        const2 = 0x13
    for j in ascii:
        c = ((ord(j) ^ const1)+const2) & 0xff
        if c == v33[i]:
            print(j, end='')
            break
