from z3 import *


# def func(a1):
#     v3 = 0

#     while a1 > 0:
#         # print(a1)
#         v3 += a1 % 10*a1 % 10*a1 % 10*(a1 % 10)
#         print(v3)
#         a1 /= 10
#         a1 = int(a1)
#     print(v3)


input = [BitVec(f'input_{i}', 32) for i in range(10)]
S = Solver()
v3 = 0
for i in range(10):
    # v3 += ((((input[i]*input[i])%10)*input[i])%10)*input[i]
    v3 += input[i]*input[i]*input[i]*input[i]

for i in range(10):
    S.add(input[i] >= 0, input[i] <= 9)

S.add(v3 == 8208)
print(S)
assert sat == S.check()

print(S.model())

for i in input:
    print(S.model()[i].as_long(), end='')


print()
# func(1799608060)
