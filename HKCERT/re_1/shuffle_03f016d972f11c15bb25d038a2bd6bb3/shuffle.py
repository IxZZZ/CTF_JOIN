# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: shuffle.py
# Compiled at: 2021-08-17 19:58:36
# Size of source mod 2**32: 281 bytes
import random
random.seed(38)
flag = b'p\xbcl\xf0Y3C#\xf5\xf8\xb0\xe6\x98%\x17\xaf\xa8\x1d\xf1\x19\xb3i\x9aj\x1e\xccx\xb7F\xea\xfa]\r\xf1X\xc1\x8e\xee'
output = b''
for c in flag:
    res = list(map(int, bin(c)[2:].rjust(8, '0')))
    pre_shuffle = [i for i in range(8)]
    random.shuffle(pre_shuffle)

    out = [0 for i in range(8)]
    for index in range(8):
        out[pre_shuffle[index]] = res[index]
        
    shuffled = int(''.join(map(str, out)), 2)
    output += bytes([shuffled])

print(output)
print(len(output))
