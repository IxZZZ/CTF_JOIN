
import random
import string
out = open('output.txt','rb').read()
random.seed(len(out))
for o in out:
    for c in string.printable:
        output = b''
        res = list(map(int, bin(ord(c))[2:].rjust(8, '0')))
        random.shuffle(res)
        shuffled = int(''.join(map(str, res)), 2)
        if shuffled == o:
            print(c,end='')
            break
