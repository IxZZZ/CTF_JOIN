def func(c, index):

    random = 80
    # c = 0xd8
    # index = 1

    s_0x4d = c ^ random
    s_0x4e = s_0x4d >> 0xd

    s_0x50 = (~(s_0x4d >> 3)) & 0x1f

    s_0x51 = (~(s_0x4d)) & 0x7

    edx = (s_0x50 << 0xb) | (s_0x4e << 8)

    edx = (s_0x51 << 5) | edx

    s_0x54 = 0 | edx

    i_d = (index+1)*3

    i_d = i_d & 0xf

    s_0x56 = s_0x54 & 0xffff

    s_0x58 = i_d & 0xffff

    esi = s_0x56 >> (s_0x58 & 0xff)

    edx = s_0x56 & 0xffff

    eax = 0x10 - s_0x58

    edx = edx << eax

    eax = edx | esi

    s_0x5a = eax & 0xffff

    return s_0x5a


def brutce_force(res, index):
    for i in range(0, 256):
        if func(i, index) == res:
            return i


print(brutce_force(0x0a00, 0))

f = open('flag.jpg.enc', 'rb')

bytes_r = f.read()
f.close()

file = open('flag.jpg', 'wb')

for i in range(0, len(bytes_r), 2):
    b = bytes_r[i:i+2]
    res = int.from_bytes(b, byteorder='little')
    res = brutce_force(res, i//2)
    file.write(bytes([res]))

file.close()
