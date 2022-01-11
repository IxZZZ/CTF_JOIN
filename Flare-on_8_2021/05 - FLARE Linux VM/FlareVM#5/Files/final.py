password = list('A'*14)

password[0] = 0x45
password[1] = 0x34
password[2] = 0x51
password[3] = 0x35
password[4] = 0x64

password[5] = 0x36

password[6] = 0x66
password[7] = 0x60
password[8] = 115
password[9] = 52
password[10] = ord('!')
password[11] = 68
password[12] = 0x35

password[13] = ord('?')


str = ''.join([chr(i) for i in password])

import string
import hashlib


print(str)

for i in string.printable:
    for j in string.printable:
        a = str.replace('?', i)
        a = a.replace('!',j )
        m = hashlib.sha256(a.encode('utf-8'))
        # print(m.hexdigest())
        # print(a)
        # print(m.hexdigest())
        if m.hexdigest() == 'b3c20caa9a1a82add9503e0eac43f741793d2031eb1c6e830274ed5ea36238bf':
            print(a)
