from z3 import *


arr = []
for i in range(6):
    arr.append(pow(31, i, 10000000))

arr = arr[::-1]
str = ''
count = 0

S = Solver()
while len(set(list(str.split(' ')))) != 457:
    try:
        msg = [BitVec(f'msg_{i}', 32) for i in range(6)]

        a = 0
        for i in range(len(msg)):
            a += msg[i]*arr[i]

        a = a % 10000000

        S.add(a == 0)

        for i in range(len(msg)):
            S.add(Or(And(msg[i] >= 48, msg[i] <= 57), And(
                msg[i] >= 65, msg[i] <= 90), And(msg[i] >= 97, msg[i] <= 122)))

        assert sat == S.check()

        ans = S.model()

        for i in msg:
            str += chr(ans[i].as_long())
        
        S.add(Or(msg[0] != ans[msg[0]].as_long(), msg[1] !=
              ans[msg[1]].as_long(), msg[2] != ans[msg[2]].as_long(), msg[3] != ans[msg[3]].as_long(), msg[4] != ans[msg[4]].as_long()))
        count += 1
        str += ' '
    except AssertionError:
        print(str)
        print('not good')
        break

print(str)
