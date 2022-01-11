import random

for i in range(10):
    #random.seed(i)
    print(random.randint(0, 18446744073709551616) % 33)
    # if random.randint(0, 18446744073709551616)% 33 == 28:
    #     print(i)
    #     break

random.seed(18)

print(random.randint(0, 18446744073709551616) % 33)
print(random.randint(0, 18446744073709551616) % 33)
print(random.randint(0, 18446744073709551616) % 33)
print(random.randint(0, 18446744073709551616) % 33)
