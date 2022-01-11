from z3 import *


def bitrev8(x):
    x = LShR(x, 4) | (x << 4)
    x = LShR(x & 0xCC, 2) | ((x & 0x33) << 2)
    x = LShR(x & 0xAA, 1) | ((x & 0x55) << 1)
    return x

# these "unoptimized" versions are constructed like a Russian doll...


def bitrev16_unoptimized(x):
    return (bitrev8(x & 0xff) << 8) | (bitrev8(LShR(x, 8)))


def bitrev32_unoptimized(x):
    return (bitrev16_unoptimized(x & 0xffff) << 16) | (bitrev16_unoptimized(LShR(x, 16)))


def bitrev32(x):
    x = LShR(x, 16) | (x << 16)
    x = LShR(x & 0xFF00FF00, 8) | ((x & 0x00FF00FF) << 8)
    x = LShR(x & 0xF0F0F0F0, 4) | ((x & 0x0F0F0F0F) << 4)
    x = LShR(x & 0xCCCCCCCC, 2) | ((x & 0x33333333) << 2)
    x = LShR(x & 0xAAAAAAAA, 1) | ((x & 0x55555555) << 1)
    return x


def bitrev64_unoptimized(x):
    # both versions must work:
    return (bitrev32_unoptimized(x & 0xffffffff) << 32) | bitrev32_unoptimized(LShR(x, 32))
    # return (bitrev32(x & 0xffffffff) << 32) | bitrev32(LShR(x, 32))

# copypasted from CADO-NFS 2.3.0, http://cado-nfs.gforge.inria.fr/download.html


def bitrev64(a):
    a = LShR(a, 32) ^ (a << 32)
    m = 0x0000ffff0000ffff
    a = (LShR(a, 16) & m) ^ ((a << 16) & ~m)
    m = 0x00ff00ff00ff00ff
    a = (LShR(a, 8) & m) ^ ((a << 8) & ~m)
    m = 0x0f0f0f0f0f0f0f0f
    a = (LShR(a, 4) & m) ^ ((a << 4) & ~m)
    m = 0x3333333333333333
    a = (LShR(a, 2) & m) ^ ((a << 2) & ~m)
    m = 0x5555555555555555
    a = (LShR(a, 1) & m) ^ ((a << 1) & ~m)
    return a


flag = [BitVec(f'flag_{i}', 64) for i in range(96)]

t = []
for i in range(12):
    a = 0
    for k in range(8):
        a = (a << 8) | (flag[i*8+k])
    t.append(a)

t0 = t[0] ^ t[4]

t1 = t[1] ^ t[5]

t2 = t[2] ^ t[6]

t3 = t[3] ^ t[7]


t4 = bitrev64(t0)

t5 = bitrev64(t1)

t6 = bitrev64(t2)

t7 = bitrev64(t3)


t0 = (0xffffffff & t5) | ((t6 >> 32) << 32)

t1 = (0xffffffff & t7) | ((t4 >> 32) << 32)

t2 = (0xffffffff & t4) | ((t5 >> 32) << 32)

t3 = (0xffffffff & t6) | ((t7 >> 32) << 32)


t4 = bitrev8(t0)

t5 = bitrev8(t1)

t6 = bitrev8(t2)

t7 = bitrev8(t3)


t0 = t4 ^ t[8]

t1 = t5 ^ t[9]

t2 = t6 ^ t[10]

t3 = t7 ^ t[11]

S = Solver()

S.add(t0 == 0xffffffffffffffff, t1 == 0xffffffffffffffff,
      t2 == 0xffffffffffffffff, t3 == 0xffffffffffffffff)

for i in range(len(flag)):
    S.add(flag[i] > 32, flag[i] < 127)

assert sat == S.check()
