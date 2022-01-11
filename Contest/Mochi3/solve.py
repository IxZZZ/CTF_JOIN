import math

limit = int('50492d761e400c2b5e22c8f253dd6f75c27e4bc84e33c2eff272476a0588fb02',16)//2941460046203168433808698735326701052265551841195155278226402
# limit = 100
n1 = 0

# for i in range(limit):
# 	n1 += 2*i-1


n1 = 2*((limit-1)*limit//2) - limit
print(n1)

n2 = 0

# for i in range(n1):
# 	n2 += math.floor(i/2)*2
# print(n2)

n1 = n1 // 2

n2 = ((n1-1)*n1//2)*2*2

print(n2)

print('key')
print((hex(n2)[2:]).encode()[:16])


