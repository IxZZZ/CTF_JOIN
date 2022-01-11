# offset = 0x000055BB1EB43220

# arr = []

# for i in range(36):
#     arr.append(ida_bytes.get_bytes(offset,1))
#     offset += 1

# print(arr)

def crc8(str, constant):
    v3 = 0
    for i in range(constant):
        v3 = ord(str[i])

# 256
arr_crc_check = [b'\xd6', b'\xd4', b'M', b'F', b'S', b'\xcd', b'>', b'\xc7', b'A', b'm', b'P', b'\x8a', b'"', b'\xbf', b',', b'\x8e', b'\t', b'\x9c', b'\x01', b'U', b'\x10', b'5', b'\xf4', b'\xc5', b'k', b'h', b'\xd8', b'O', b'\xd5', b'\x15', b'\x13', b'\xa8', b'\x08', b'\xd3', b'B', b'2', b'T', b'\x06', b'\x94', b'\xa1', b'\xe0', b'\xfb', b'\xad', b'\xff', b'_', b'\x9e', b'1', b'\x82', b'\x02', b'\xca', b'\x1e', b'\xf2', b'J', b'\xd7', b'\xe2', b'G', b'H', b'f', b'\x80', b'\x14', b'g', b'\xda', b"'", b'-', b'b', b'\xe8', b'@', b'\x11', b'#', b'!', b'\x84', b'\x81', b't', b'\x17', b'\xbe', b'\xce', b'\x9b', b'\x92', b'\xb5', b'\x0e', b'\xc6', b'\xf0', b'\x99', b'\xf7', b'\xa6', b'\xdf', b':', b'v', b'\xdd', b'|', b'\xd1', b'\xf6', b'\xa9', b'\xe9', b'\xb7', b'\x07', b'\x97', b'z', b'\xc2', b'~', b'\x90', b'\xb3', b'L', b'0', b']', b'\xfd', b'E', b'\x85', b'\xa3', b'u', b'\xe3', b'\xf3', b'I', b'\xbd', b'\r', b'8', b'\xb4', b'\x8b', b'\xb9', b'\xfa', b'\xaa', b'Y', b'\xb2', b'+', b'j', b'\xcf', b'\x0b', b'\xe6',
    b'\x05', b'c', b'<', b'\xbc', b'\xe5', b'\x87', b'y', b'\x88', b'\xa5', b'\x03', b'4', b'C', b'\xef', b'\x1d', b'}', b'\x89', b'\xf1', b'X', b'3', b'\xb1', b'x', b'\x83', b'\x95', b'\x7f', b'\xdb', b'{', b'\xb6', b'\xf5', b'\x1b', b'/', b'\xba', b'7', b'\x8d', b'\x18', b'\x12', b'\xd0', b's', b'\xe7', b'?', b'p', b'\xa7', b'\x0c', b'\n', b'd', b'\x9f', b'q', b'l', b'\xae', b'(', b'\xeb', b'\x96', b'\xb8', b'\xa2', b'\x19', b'\x8f', b'\x86', b'\xd9', b'\x0f', b'\xdc', b'\xc9', b'\xf9', b'9', b'^', b'\xab', b'Q', b'\xcb', b'\xc1', b'%', b' ', b'e', b'D', b'\xee', b'\\', b';', b'\xa4', b'\x1f', b'\xcc', b'\xaf', b')', b'\xc8', b'*', b'`', b'\xac', b'a', b'Z', b'\xf8', b'[', b'K', b'\x93', b'\xec', b'\x8c', b'\x9d', b'\xa0', b'\xc3', b'\xde', b'\x98', b'\xbb', b'6', b'\xe4', b'\xea', b'r', b'\x00', b'=', b'\xb0', b'$', b'N', b'w', b'o', b'R', b'\xfe', b'\xc0', b'\x1a', b'\x91', b'i', b'V', b'.', b'\x9a', b'\x16', b'\xfc', b'\x04', b'\xe1', b'&', b'\x1c', b'W', b'\xed', b'\xd2', b'n', b'\xc4']

# 36
arr_xor_check = [b'\t', b'\x16', b'\x17', b'\x0f', b'\x17', b'V', b'\x16', b'D', b':', b'\x18', b'S', b'o', b'\x14', b'\x03', b'*', b'\x06',
                 b'o', b'1', b'\x1c', b'G', b'*', b'\x06', b'-', b'_', b'Q', b'\x1b', b'\x00', b'F', b'J', b'\x00', b'\x04', b'U', b'f', b'P', b'\x01', b'L']


# str1 = 'w1nR4rs'

# str_6_place = ''
# for i in range(len(str1)):
#     crc8_res = arr_crc_check.index(ord(str1[i]))

count = 0
str = list('rarctf')
for i in arr_xor_check:
    str[count] = chr(ord(str[count])^int.from_bytes(i,byteorder='little'))
    count += 1
    if count == 6:
        print(''.join(str),end='')
        count = 0