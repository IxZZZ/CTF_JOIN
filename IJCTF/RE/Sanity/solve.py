flag = 'IJCTF{simple_sanity_check_for_babies}'
arr = [0, 0, 0, 0, 0, 0, 0xa, 6, 0x18, 0x2f, 8, 0xc, 0x3b, 0x2c, 0xf, 1, 0x1d, 0x2b,
       0x1F, 0x3e, 0xF, 4, 0x3a, 5, 4, 0x2d, 0x39, 6, 6, 0, 0x10, 0x8, 5, 1, 0x11, 0x4c, 0, 0]

j = 0
for i in flag:
    print(chr(ord(i) ^ arr[j]), end='')
    j = j + 1
