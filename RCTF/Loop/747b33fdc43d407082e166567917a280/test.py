from z3 import *


def bitrev8(x):
    x = LShR(x, 4) | (x << 4)
    x = LShR(x & 0xCC, 2) | ((x & 0x33) << 2)
    x = LShR(x & 0xAA, 1) | ((x & 0x55) << 1)
    return x


def bitrev64(a):
    a = (a >> 32) ^ (a << 32)
    a = a & (0xffffffffffffffff)
    m = 0x0000ffff0000ffff
    a = ((a >> 16) & m) ^ ((a << 16) & ~m)
    a = a & (0xffffffffffffffff)
    m = 0x00ff00ff00ff00ff
    a = ((a >> 8) & m) ^ ((a << 8) & ~m)
    a = a & (0xffffffffffffffff)
    m = 0x0f0f0f0f0f0f0f0f
    a = ((a >> 4) & m) ^ ((a << 4) & ~m)
    a = a & (0xffffffffffffffff)
    m = 0x3333333333333333
    a = ((a >> 2) & m) ^ ((a << 2) & ~m)
    a = a & (0xffffffffffffffff)
    m = 0x5555555555555555
    a = ((a >> 1) & m) ^ ((a << 1) & ~m)
    a = a & (0xffffffffffffffff)
    return a & (0xffffffffffffffff)


def bitrev8_py(x):
    x = (x >> 4) | (x << 4)
    x = ((x & 0xCC) >> 2) | ((x & 0x33) << 2)
    x = ((x & 0xAA) >> 1) | ((x & 0x55) << 1)
    return x


x = BitVec('x', 64)

x = 0x4142434445464748


a = bitrev64(x)
print(a)

b = bin(a)[2:]
print((bin(x)[2:])[::-1])
print('000'+b)
b = int(b[::-1], 2)
print(hex(b))
