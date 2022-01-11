# /usr/bin/env python3
import pickle
import sys

# Check version >= 3.9
if sys.version_info[0] != 3 or sys.version_info[1] < 9:
    print("Check your Python version!")
    exit(0)

# This function is truly amazing, so do not fix it!


def amazing_function(a, b, c=None):
    print('---')
    print(a, b, c)
    print('---')
    if type(b) == int:
        return a[b]
    else:
        return (
            f"CORRECT! The flag is: ACSC{{{c.decode('ascii')}}}" if a == b else "WRONG!"
        )


with open("rick.pickle", "rb") as f:
    pickle_rick = f.read()
# Wubba lubba dub-dub!!
rick_says = b"aCSC{ lubba dub-dub!!"  # What is the right input here?
# assert type(rick_says) == bytes and len(rick_says) == 21


pickle.loads(pickle_rick)


# t = b'd\x01}\x02zB|\x00\\\x02}\x03}\x04|\x01d\x02\x16\x00|\x02k\x02r0|\x04}\x00|\x01d\x02\x1c\x00}\x01d\x03|\x02\x18\x00}\x02n\x14|\x03}\x00|\x01d\x02\x1c\x00}\x01d\x03|\x02\x18\x00}\x02W\x00q\x04\x01\x00\x01\x00\x01\x00|\x00d\x01\x19\x00\x06\x00Y\x00S\x000\x00q\x04d\x00S\x00'

# t1 = b'\x00\x01\x04\x02\x02\x01\x08\x01\x0c\x01\x04\x01\x08\x01\n\x02\x04\x01\x08\x01\x0c\x01\x06\x01'

# tu1 = (0, 2, 1)

# tu2 = ('a', 'b', 'c', 'a0', 'a1')

# a = amazing_function.__code__

# b = type(a)(2,0,0,5,6,67,t,tu1,(),tu2,'something_suspicious.py','search',45,t1,(),())
# x = type(amazing_function)

# print(b)
# c = x(b,{})

# print(c(b'abc',b'def'))


t = b'|\x00\xa0\x00\xa1\x00}\x01g\x00}\x02d\x01}\x03|\x03|\x01k\x00rvd\x02\\\x02}\x04}\x05|\x05|\x01k\x00rN|\x04|\x05d\x03\x17\x00|\x00|\x03|\x05\x17\x00|\x01\x16\x00\x19\x00\x14\x007\x00}\x04|\x05d\x037\x00}\x05q |\x04d\x04;\x00}\x04|\x04d\x05k\x00sbJ\x00\x82\x01|\x02\xa0\x01|\x04\xa1\x01\x01\x00|\x03d\x037\x00}\x03q\x10|\x02S\x00'

t1 = b'\x00\x01\x08\x01\x04\x01\x04\x01\x08\x01\x08\x01\x08\x01\x1c\x01\n\x01\x08\x01\x0c\x01\n\x01\n\x01'


tu1 = (None, 0, (0, 0), 1, 257, 256)

tu2 = ('a', 'ln', 'arr', 'i', 's', 'j')

tu3 = ('__len__', 'append')

x = type(amazing_function)

a = amazing_function.__code__

b = type(a)(1, 0, 0, 6, 5, 67, t, tu1, tu3, tu2,
            'something_suspicious.py', 'mix', 61, t1)

d = x(b, {})

# print(d.__code__.co_argcount)

print(d(rick_says))
