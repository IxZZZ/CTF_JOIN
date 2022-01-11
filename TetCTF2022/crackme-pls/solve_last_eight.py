from z3 import *

win_addr = 0x401220

# input = [BitVec(f'input_{i}',64) for i in range(8)]
# rax = 0
# for i in range(8):
#     rax = rax | (input[i]&0xff)
#     rax = rax <<8
rax = BitVec('rax',64)
# rax = 0x4141414141414141
rcx = 0x3131312121613301
rdx = rcx^rax
rsi = rcx
rdx = rdx + rcx
rcx = rcx &rax
rsi = (~rsi)|rax
rdx = rdx - rcx
rax = rdx+ rsi + 1

S = Solver()

S.add(rax == win_addr)

print(S)
assert S.check() == sat
print(S.model())

