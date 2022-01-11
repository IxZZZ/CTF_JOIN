
import string


def s16(value):
    return -(value & 0x8000) | (value & 0x7fff)


offset = 0x0000561B808DD020 + 7 + 0x40e


ascii_char = string.printable
loop = 100
while True:
    b = ida_bytes.get_bytes(offset, 7)
    #print(hex(offset), '-', arr)
    for c in ascii_char:
        if ord(c) ^ b[0] == 0x48:
            arr = []
            for k in b:
                arr.append(k ^ ord(c))

            print(c, end='')
            #print(hex(offset), '-', arr)
            inc = (arr[6]*((0xff+1)**3) + arr[5] *
                   ((0xff+1) ** 2) + arr[4]*(0xff+1) + arr[3])
            # print(inc)
            offset += 7 + s16(inc)

            break
    loop -= 1
    if loop == 0:
        break
