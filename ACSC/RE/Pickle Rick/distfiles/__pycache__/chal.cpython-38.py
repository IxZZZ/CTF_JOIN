# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: chal.py
# Compiled at: 2021-09-19 01:04:42
# Size of source mod 2**32: 2193 bytes


def amazing_function(a, b, c=None):
    print('---')
    print(a, b, c)
    print('---')
    if type(b) == int:
        return a[b]
    if a == b:
        return f"CORRECT! The flag is: ACSC{{{c.decode('ascii')}}}"
    return 'WRONG!'


rick_says = 'aCSC{ lubba dub-dub!!'
t = b'|\x00\xa0\x00\xa1\x00}\x01g\x00}\x02d\x01}\x03|\x03|\x01k\x00rvd\x02\\\x02}\x04}\x05|\x05|\x01k\x00rN|\x04|\x05d\x03\x17\x00|\x00|\x03|\x05\x17\x00|\x01\x16\x00\x19\x00\x14\x007\x00}\x04|\x05d\x037\x00}\x05q |\x04d\x04;\x00}\x04|\x04d\x05k\x00sbJ\x00\x82\x01|\x02\xa0\x01|\x04\xa1\x01\x01\x00|\x03d\x037\x00}\x03q\x10|\x02S\x00'
t1 = '\x00\x01\x08\x01\x04\x01\x04\x01\x08\x01\x08\x01\x08\x01\x1c\x01\n\x01\x08\x01\x0c\x01\n\x01\n\x01'
tu1 = (None, 0, (0, 0), 1, 257, 256)
tu2 = ('a', 'ln', 'arr', 'i', 's', 'j')
tu3 = ('__len__', 'append')
x = type(amazing_function)
a = amazing_function.__code__
b = type(a)(1, 0, 0, 6, 5, 67, t, tu1, tu3, tu2, 'something_suspicious.py', 'mix', 61, t1)
d = x(b, {})
print(d(rick_says))