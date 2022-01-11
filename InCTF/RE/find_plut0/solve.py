import string
s1 = list('inctf{U_Sur3_m4Te?}')

a1 = list('A'*30)
s1_0 = []
for i in s1:
    s1_0.append(ord(i))

s1 = s1_0
print(s1)

# s1[0] = (*a1 ^ 2) - 31
a1[0] = (s1[0] + 31) ^ 2


# s1[1] = ((a1[1] % 2) ^ *a1) - 29
#s1[2] = (4 * a1[1]) ^ 0x97

a1[2] = int((s1[1] ^ 0x97)/4)


#s1[3] = a1[2] ^ 0xA0

a1[2] = s1[3] ^ 0xA0

#s1[4] = (a1[3] ^ 0x4D) + 7

a1[3] = (s1[4]-7) ^ 0x4d

#s1[5] = 4 * a1[5] - 1

a1[5] = int((s1[5]+1)/4)

#s1[3] = a1[4] + 116

a1[4] = s1[3] - 116

#s1[6] = a1[6] + 21

a1[6] = s1[6]-21


#s1[7] = a1[7] - 20

a1[7] = s1[7]+20

#s1[8] = a1[8] ^ 0x63

a1[8] = s1[8] ^ 0x63

#s1[10] = a1[9] ^ 0x42

a1[9] = s1[10] ^ 0x42

#s1[9] = (a1[10] ^ 3) - a1[8] + 54
a1[10] = (s1[9]-54+a1[8]) ^ 3


#s1[11] = a1[11] + 51
a1[11] = s1[11] ^ 51

#s1[11] = a1[12] ^ 0xB3

a1[12] = s1[11] ^ 0xb3

#s1[12] = (a1[13] + 18) ^ 0x1A

a1[13] = (s1[12] ^ 0x1a)-18


#s1[13] = a1[14] - 7

a1[14] = s1[13]+7

#s1[14] = a1[15] - 37
a1[15] = s1[14]+37

#s1[15] = a1[17] ^ 0xE5
a1[17] = s1[15] ^ 0xe5

#s1[16] = (a1[18] & 0x36) + 53
a1[18] = ord('p')

#s1[14] = a1[19] ^ 0x34
a1[19] = 0x34 ^ s1[14]

#s1[17] = a1[20] ^ 0xFD

a1[20] = s1[17] ^ 0xfd

# s1[18] = ((int)a1[20] >> a1[21]) ^ 0x1C
# ??
a1[21] = 1

print(a1)


# a1[0] = input[0] - 50 + input[1]
# a1[1] = input[1] - 100 + input[2]
# a1[2] = 4 * input[2]
# a1[3] = input[3] ^ 0x46
# a1[4] = 36 - (input[3] - input[4])
# a1[6] = input[6] * input[5] + 99
# a1[7] = (char)(input[6] ^ input[7])
# a1[8] = (input[7] + 45) ^ input[8]
# a1[9] = (input[9] & 0x37) - 3
# a1[11] = input[11] - 38
# a1[12] = 4 * ((char)(input[12] ^ input[6]) + 4)
# a1[5] = (input[21] - input[4]) ^ 0x30
# a1[13] = input[13] - input[14] - 1
# a1[10] = input[17] - input[16] + 82
# a1[16] = 6 * (char)(input[18] ^ input[19]) + 54
# a1[17] = input[21] + 49 + (input[20] ^ 0x73)
# a1[14] = input[22]
# a1[18] = input[23] ^ 0x42
# a1[15] = input[26] + 5
# a1[19] = input[25] - input[26] / 2 - 55
# a1[20] = 4 * input[27] - (input[28] + 128)
# a1[21] = input[29] - 32

input = list('A'*30)

input[29] = a1[21]+32

# input 27,28?

input[26] = a1[15]-5

input[25] = a1[19]+55+int(input[26]/2)

# input[24]

input[23] = a1[18] ^ 0x42

input[22] = a1[14]

# input 20,21

# input18,19

print(input)


str_ascii = string.printable
print(a1[20])
for i in str_ascii:
    for j in str_ascii:
        if (ord(i)*4 - ord(j)-128) == a1[20]:
            print(i, j)


# str_ascii = string.printable
# print(a1[6])
# for i in str_ascii:
#     for j in str_ascii:
#         if ((ord(i) * ord(j))+99) & 0xff == a1[6]:
#             print(i, j)
