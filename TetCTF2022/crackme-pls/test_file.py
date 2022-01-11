import string
arr_const = [121, 148, 249, 108, 0, 198, 52, 253, 133, 156, 119, 148, 246, 218, 252, 218, 242, 64, 156, 123, 116, 220,
             109, 215, 101, 245, 50, 197, 104, 74, 48, 87, 9, 41, 22, 25, 249, 249, 250, 232, 206, 112, 197, 216, 28, 102, 193, 101]
arr_compare = [194, 70, 82, 103, 8, 95, 185, 247, 153, 22, 82, 34, 71, 77, 78, 240, 105, 6, 80, 79, 196, 187, 238,
               159, 67, 233, 202, 140, 51, 199, 122, 92, 65, 126, 98, 133, 205, 109, 100, 10, 22, 81, 151, 71, 193, 116, 158, 0x43]
r14 = 0
ebx = 0
r11 = arr_const[0]
input = [ord(i)
         for i in '4is_0ft4hc4__u00_r00abgf__drt_zcw_l0d3nm30twntl3']

print('h3ll', end='')
input = [ord(i) for i in string.printable]
arr_final = []
while True:
    for inp in input:
        for _ in range(1):
            # ebx  = 1 # index
            # r14 = 0x79 # first = 0
            # r11 = 0x94 # first = arr_const[index]
            ecx = inp

            eax = arr_const[ebx]

            ebp = (~eax) & ecx

            ecx = ((~ecx) & eax) + ebp

            eax = (r14 & 0xff) ^ ecx

            ecx = (r11 & 0xff)

            ebp = eax & ecx

            eax = eax ^ ecx
            final = eax+ebp*2

            # arr_final.append(final & 0xff)

            # r14 = arr_const[ebx]

            # eax = ((ebx+ebx) | 0xFFFFFFFC)

            # ebx = ((ebx^1)+eax)+4
            # r11 = arr_const[ebx+1]
            if (final & 0xff) == arr_compare[ebx]:
                # print(hex(final), end=', ')
                print(chr(inp), end='')
                r14 = arr_const[ebx]
                ebx += 1
                if ebx < 0x30:
                    r11 = arr_const[ebx]
                else:
                    r11 = 0
                if ebx > 0x2f:
                    print('!!!!!111')
                    exit()
                break

            # print(hex(ebx&0xff))
