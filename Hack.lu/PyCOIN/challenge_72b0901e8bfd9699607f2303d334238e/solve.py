# from hashlib import md5
# import string

# for i in string.printable:
#     md = md5(ord(i)*b'a')
#     if md.digest()[0]-1 == ord('g'):
#         print(i)
from z3 import *

flag = [BitVec(f'flag_{i}', 8) for i in range(16)]

S = Solver()

S.add(flag[0] == 102)  # 'f'
S.add(flag[1] == 108)  # 'l'
S.add(flag[2] == 97)  # 'a'
S.add(flag[3] == 103)  # 'g'


S.add(flag[4] == flag[11]*3 - 42)


# sum(flag)-1322 = flag[5]  # flag[5] = '5'

s = 0
for i in range(len(flag)):
    S.add(flag[i] >= 32, flag[i] <= 126)
    s += flag[i]
S.add(s-1322 == ord('5'))
S.add(flag[5]==ord('5'))

S.add(flag[6]+flag[7]+flag[10] == 260)

S.add((flag[7]-48)*10+(flag[7]-48)+1 == flag[9])

S.add(flag[8] % 17 == 16)
flag[9] = flag[8]*2
#md5.digest((flag[10]*b'a'))[0]-1 == flag[3]
S.add(flag[10] == ord('e'))
S.add(flag[11] == 55)
S.add(flag[12] == flag[14]/2 - 2)
S.add(flag[13] == ((flag[10]*flag[8]) % 32)*2 - 1)
S.add(flag[14] == (flag[12] ^ flag[9] ^ flag[15])*3-23)
S.add(flag[15] == 125)


assert sat == S.check()
res = S.model()
print(res)

for i in range(len(flag)):
    if i != 9 :
        print(chr(res[flag[i]].as_long()),end='')
    else:
        print(chr(100),end='')