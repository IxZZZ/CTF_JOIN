from z3 import *

const_build = 0x323030B5052D012C

const_v5_final = 0x8A0B76BC

input_1 = Int('input_1')
input_2 = Int('input_2')
input_3 = Int('input_3')

S = Solver()
S.add(1620*input_2+5447*input_3+17170*input_1 ==
      (const_build ^ 0x2ED0F8B0) & 0xffffffff)
S.add(9543*input_3+19218*input_1+27870 *
      input_2 == (const_build >> 32) ^ 0x63987AEB)

S.add(7287*input_3+11210*input_1+24874*input_2 == const_v5_final^0xB6DDCFF6)

assert sat == S.check()

print(S.model())


