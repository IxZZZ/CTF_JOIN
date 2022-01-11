from z3 import *

dict_db = {}

couple_char = [BitVec(f'couple_char_{i}', 16) for i in range(2)]

state = (couple_char[0] << 8) + couple_char[1]
for k in range(0x76d2):
    state = 21727 * (18199 * ((25561 * (31663 * (-1635 *
                     (state ^ 0x6BB1) - 16196) + 14122)) ^ 0x448C) - 11258)
    state = state & 0xffff

S = Solver()

for i in range(len(couple_char)):
    S.add(couple_char[i] >= 65, couple_char[i] <= 66)

S.add(state & 0xffff == 0x09d3)

assert sat == S.check()

ans = S.model()
print(ans)
