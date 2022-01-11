from z3 import *


flag_1 = 'AAAAAAAAAA'
flag_2 = 'BBBBBBBBBB'

haft_first = 0
haft_last = 0


for i in range(len(flag_1)):
    haft_first = (haft_first << 8) | ord(flag_1[i])
    haft_last = (haft_last << 8) | ord(flag_2[i])

print(hex(haft_first))
print(hex(haft_last))