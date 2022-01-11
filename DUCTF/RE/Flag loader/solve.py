from z3 import *


def solve_check1():
    five_chars = [BitVec(f'char_{i}', 16) for i in range(5)]

    arr = [68, 85, 67, 84, 70]

    sum = 0
    for i in range(len(arr)):
        sum += arr[i] ^ five_chars[i]

    S = Solver()

    S.add(sum & 0xff == 0)

    for i in range(len(arr)):
        S.add(five_chars[i] >= 33, five_chars[i] <= 126)

    assert sat == S.check()

    ans = S.model()

    print(ans)

    res = []
    for i in five_chars:
        print(chr(ans[i].as_long()), end='')
        res.append(ans[i].as_long())

    return res


def solve_check2(sum, v1):
    x, y = BitVecs('x y', 33)
    S = Solver()
    v1 = IntVal(v1)
    v1 = Int2BV(v1, 33)
    S.add(x > sum, y > sum, (x+y) & 0xffffffff ==
          sum, (x*y) & 0xffff > 0x3b, (x*y*v1) & 0x3fffff == 0)

    assert S.check() == sat
    ans = S.model()
    print(ans)
    print(len(bin(ans[x].as_long())[2:]))
    print(len(bin(ans[y].as_long())[2:]))
    return ans[x].as_long() * ans[y].as_long()


def solve_check3(sum, mul):
    x1, x2, x3, x4, x5 = BitVecs('x1 x2 x3 x4 x5', 32)

    S = Solver()
    S.add(ULT(x1, x2))
    S.add(ULT(x2, x3))
    S.add(ULT(x3, x4))
    S.add(ULT(x4, x5))
    S.add((x1+x2+x3+x4+x5) & 0xffffffff ==
          sum)
    cal = (x3-x2)*(x5-x4)
    c = IntVal(mul)
    S.add(UGT(cal & 0xffff, 0x3b), (cal*Int2BV(c, 32)) & 0xffffffff == 0)
    assert S.check() == sat
    ans = S.model()
    print(ans)
    res = [ans[x1].as_long(), ans[x2].as_long(), ans[x3].as_long(),
           ans[x4].as_long(), ans[x5].as_long()]
    ret = ((res[2]-res[1])*(res[4]-res[3])) & 0xffffffff
    print(ret)
    print((ret*mul) & 0xffffffff)


res = solve_check1()

v1 = 1
for i in range(len(res)):
    v1 *= res[i]*(i+1)
print()
print(v1 & 0xffffffff)

sum = int(input('sum2: '))
v2 = solve_check2(sum, v1)


mul = (v1*v2) & 0xffffffff
print(mul)
sum = int(input('sum3: '))

solve_check3(sum, mul)
