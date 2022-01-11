import string
str_cat = 'oI!&}IusoKs ?Ytr'[::-1]
str_cat_xor = '41!ce1337'

str_input_cat = ''


for i in range(len(str_cat)):
    str_input_cat += chr(ord(str_cat[i]) ^
                         ord(str_cat_xor[i % len(str_cat_xor)]))
    print(str_input_cat)

print(str_input_cat[::-1])

Foo = '\\xDE\\xAD\\xBE\\xEF'
# \xDE\xAD\xBE\xEF
print(len(Foo))


def ror(v, s):
    b = s % 8
    res = (v << b | v >> (8-b)) & 0xff
    return res


def cal(c, t):
    b = ror(c, 114)
    b += 222
    b = b & 0xff
    b ^= t
    b = b & 0xff
    b -= 127
    b = b & 0xff
    if b < 0:
        print('neg')
    b = rol(b, 6)
    return b


ascii = string.printable

str_caterpillar = "\0R\u009c\u007f\u0016ndC\u0005î\u0093MíÃ×\u007f\u0093\u0090\u007fS}­\u0093)ÿÃ\f0\u0093g/\u0003\u0093+Ã¶\0Rt\u007f\u0016\u0087dC\aî\u0093píÃ8\u007f\u0093\u0093\u007fSz­\u0093ÇÿÃÓ0\u0093\u0086/\u0003q"
str_compute = 'c4t3rp1114rz_s3cr3t1y_ru13_7h3_w0r1d'
print(ascii)

# str_caterpillar = ['5c', '30', '52', '5c', '75', '30', '30', '39', '63', '5c', '75', '30', '30', '37', '66', '5c', '75', '30', '30', '31', '36', '6e', '64', '43', '5c', '75', '30', '30', '30', '35', 'ee', '5c', '75', '30', '30', '39', '33', '4d', 'ed', 'c3', 'd7', '5c', '75', '30', '30', '37', '66', '5c', '75', '30', '30', '39', '33', '5c', '75', '30', '30', '39', '30', '5c', '75', '30', '30', '37', '66', '53', '7d', 'ad', '5c', '75', '30', '30', '39', '33', '29', 'ff', 'c3', '5c', '66', '30', '5c', '75', '30', '30', '39', '33', '67', '2f', '5c', '75', '30', '30', '30', '33', '5c', '75', '30', '30',
#                    '39', '33', '2b', 'c3', 'b6', '5c', '30', '52', '74', '5c', '75', '30', '30', '37', '66', '5c', '75', '30', '30', '31', '36', '5c', '75', '30', '30', '38', '37', '64', '43', '5c', '61', 'ee', '5c', '75', '30', '30', '39', '33', '70', 'ed', 'c3', '38', '5c', '75', '30', '30', '37', '66', '5c', '75', '30', '30', '39', '33', '5c', '75', '30', '30', '39', '33', '5c', '75', '30', '30', '37', '66', '53', '7a', 'ad', '5c', '75', '30', '30', '39', '33', 'c7', 'ff', 'c3', 'd3', '30', '5c', '75', '30', '30', '39', '33', '5c', '75', '30', '30', '38', '36', '2f', '5c', '75', '30', '30', '30', '33', '71']


# res = ''
# for i in range(len(str_caterpillar)):
#     print('check', int(str_caterpillar[i],16), '->{', end='')
#     for c in ascii:
#         if cal(ord(c), ord(str_compute[i % len(str_compute)])) == int(str_caterpillar[i], 16):
#             res+=c
#             print(c,end='')
#     print('}')


# print(res[::-1])

def rol(v, s):
    b = s % 8
    res = (v >> b | v << (8-b)) & 0xff
    return res


arr_res = []
str_caterpillar = str_caterpillar[::-1]
for i in range(len(str_caterpillar)):
    # c = int(str_caterpillar[i],16)
    c = ord(str_caterpillar[i])
    b = rol(c, 6)
    b += 127
    b = b & 0xff
    b = (b ^ ord(str_compute[i % len(str_compute)])) & 0xff
    b -= 222
    b = b & 0xff
    b = rol(b, 2)
    arr_res.append(b)

print(arr_res)
str_res = ''
for i in arr_res:
    str_res += chr(i)

print(str_res[::-1])


# for i in arr_res:
#     print(chr(i),end='')


print(ord('A') ^ ror(ord('l'), 5))

print(ror(ord('A'), 3))


arr_dream = [0xc0, 0xc0, 0x0d, 0xf0, 0xad, 0xba, 0xa7, 0x0e]

str_hex = "3c3cf1df89fe832aefcc22fc82017cd57bef01df54235e21414122d78a9d88cfef3cf10c829ee32ae4ef01dfa1951cd51b7b22fc82433ef7ef418cdf8a9d802101ef64f9a495268fef18d52882324f217b1bd64b82017cd57bef01df255288f7593922712c958029e7efccdf081f8808a6efd5287595f821482822f6cb95f821cceff4695495268fefe72ad7821a67ae0060ad"
arr_hex = []
for i in range(0, len(str_hex), 2):
    arr_hex.append(int(str_hex[i:i+2], 16))

arr_before_xor = []

for i in range(len(arr_hex)):
    arr_before_xor.append(arr_hex[i] ^ arr_dream[i % len(arr_dream)])

print(arr_before_xor)
array = list('A'*239)

array[4] = "\u000f"
array[5] = "\u0005\u0006\u0005\u0005\u0006"
array[6] = "\u001d\u001d\u001d\u001d\u001d"
array[7] = "\u0015\u0015\u0015\u0016\u0016"
array[8] = "nmmnmn"
array[9] = "ffff"
array[10] = "~}}~"
array[11] = "uvvu"
array[12] = "\0"
array[13] = "FFFF"
array[14] = "^]]^"
array[15] = "UVVU"
array[36] = "\f\u000f\f\u000f\f\f"
array[37] = "\u0004\a\u0004\u0004\a\u0004"
array[38] = "\u001f\u001c\u001c\u001c\u001c"
array[39] = "\u0014\u0014\u0014\u0014\u0017"
array[40] = "ol"
array[41] = "gg"
array[42] = "||\u007f|"
array[43] = "twtt"
array[44] = "OL"
array[45] = "GG"
array[46] = "\\\\_\\"
array[47] = "TWTT"
array[68] = "\0"
array[69] = "\0"
array[70] = "\u001c\u001c\u001f\u001f\u001f"
array[71] = "\u0017\u0017\u0017\u0014\u0014\u0014"
array[72] = "olll"
array[73] = "dggg"
array[74] = "|\u007f|"
array[75] = "wwtt"
array[76] = "OLLL"
array[77] = "DGGG"
array[78] = "\\_\\"
array[79] = "WWTT"
array[100] = "\0"
array[101] = "\u0005\u0006\u0005\u0006\u0005"
array[102] = "\u001d\u001d\u001d\u001e\u001e"
array[103] = "\u0016\u0015\u0016\u0015\u0016\u0015"
array[104] = "nmnm"
array[105] = "fef"
array[106] = "}}}"
array[107] = "\0"
array[108] = "NMNM"
array[109] = "FEF"
array[110] = "]]]"
array[111] = "\0"
array[132] = "\n\n\n\n\n"
array[133] = "\u0001\u0001\u0002\u0002\u0001\u0001"
array[134] = "\u001a\u001a\u001a\u001a\u0019"
array[135] = "\0"
array[136] = "ijj"
array[137] = "babb"
array[138] = "y"
array[139] = "\0"
array[140] = "IJJ"
array[141] = "BABB"
array[142] = "Y"
array[143] = "\0"
array[164] = "\0"
array[165] = "\0\u0003\u0003\u0003\u0003\0"
array[166] = "\u001b\u001b\u001b\u001b\u001b"
array[167] = "\u0010\u0013\u0013\u0013\u0010"
array[168] = "k"
array[169] = "``"
array[170] = "{{x"
array[171] = "\0"
array[172] = "K"
array[173] = "@@"
array[174] = "[[X"
array[175] = "\0"
array[196] = "\b\v\b\b\b"
array[197] = "\0\u0003\0\u0003\0\u0003"
array[198] = "\u001b\u0018\u0018\u0018\u0018"
array[199] = "\0"
array[200] = "hhkh"
array[201] = "c`"
array[202] = "xxx{"
array[203] = "\0"
array[204] = "HHKH"
array[205] = "C@"
array[206] = "XXX["
array[207] = "\0"
array[228] = "\t\n\n\n\n\t"
array[229] = "\u0002\u0001\u0001\u0002\u0001"
array[230] = "\u001a\u001a\u0019\u0019\u0019"
array[231] = "\u0011\u0011\u0012\u0012\u0011\u0011"
array[232] = "jji"
array[233] = "bbb"
array[234] = "yzz"
array[235] = "qqrrqr"
array[236] = "JJI"
array[237] = "BBB"
array[238] = "YZZ"


def xor_array_and_compare(array, c, str):
    index = rol(ord(c), 3)

    if len(array[index]) != len(str):
        return False
    for i in range(len(array[index])):
        if ord(c) ^ ror(ord(array[index][i]), 5) != ord(str[i]):
            return False
    return True


strs = ''.join([chr(i) for i in arr_before_xor])
print(len(strs.split('/')))
ascii = string.printable
for str in strs.split('/'):
    for c in ascii:
        if xor_array_and_compare(array, c, str):
            print(c,end='')

#corctf{4l1c3_15_1n_d33p_tr0ubl3_b3c4us3_1_d1d_n0t_s4v3_h3r!!: c}
