s1 = list('A'*12)
s1[0] = 0x45481D1217111313
s1[1] = 0x95F422C260B4145
s1[2] = 0x541B56563D6C5F0B
s1[3] = 0x585C0B3C2945415F
s1[4] = 0x402A6C54095D5F00
s1[5] = 0x4B5F4248276A0606
s1[6] = 0x6C5E5D432C2D4256
s1[7] = 0x6B315E434707412D
s1[8] = 0x5E54491C6E3B0A5A
s1[9] = 0x2828475E05342B1A
s1[10] = 0x60450073B26111F
s1[11] = 0xA774803050B0D04

c = 'r'

print(s1)


print(c, end='')

k = 0
for i in s1:
    while (i & 0xffff) != 0:
        if k >= 0x61:
            print()
            break
        c = chr(ord(c) ^ (i & 0xff))
        print(c,end='')
        i = i >> 8
        k += 1
