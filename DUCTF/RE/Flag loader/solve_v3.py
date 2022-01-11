from z3 import *


def solve_check3(sum):

    # v1 = BitVecVal(v1,32)
    # v2 = BitVecVal(v2,32)
    x1, x2, x3, x4, x5 = BitVecs('x1 x2 x3 x4 x5', 32)

    S = Solver()
    S.add(ULT(x1, x2))
    S.add(ULT(x2, x3))
    S.add(ULT(x3, x4))
    S.add(ULT(x4, x5))
    S.add((x1+x2+x3+x4+x5) & 0xffffffff ==
          sum)
    cal = (x3-x2)*(x5-x4)
    v1 = 2136735744
    c = IntVal(v1)
    # S.add((cal*Int2BV(c, 32)) & 0xffffffff == 0x3c)
    S.add(UGL(cal,0x3b))
    assert S.check() == sat
    ans = S.model()
    print(ans)
    res = [ans[x1].as_long(), ans[x2].as_long(), ans[x3].as_long(),
           ans[x4].as_long(), ans[x5].as_long()]
    ret = ((res[2]-res[1])*(res[4]-res[3])) & 0xffffffff
    print(ret)


sum = int(input('sum3: '))
solve_check3(sum)
