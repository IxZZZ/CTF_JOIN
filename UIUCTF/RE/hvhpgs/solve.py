from math import sqrt
import string


def check_prime(number):
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return False

    return True


def rot(str, n):
    res = ''
    for i in str:
        if i != '_':
            res += chr((ord(i)-97-n) % 26+97)
        else:
            res += i

    return res


def un_shift(str, n):
    res = '0'*len(str)
    res = list(res)
    for i in range(len(str)):
        res[i] = str[(i-n) % len(str)]

    return ''.join(res)


prime_list = []

index = 1
i = 2
while True:
    if index > 1337:
        break
    if check_prime(i) == True:
        prime_list.append(i)
        index += 1
    i += 1

str = string.ascii_lowercase

res = ''

target = 'azeupqd_ftq_cgqefuaz_omz_ymotuzqe_ftuzwu_bdabaeq_fa_o'
print(len(prime_list))
for i in range(1336, -1, -1):
    target = un_shift(target, prime_list[i])
    target = rot(target, prime_list[i])

print(target)


out = 'ccddddeeeecc'
print(prime_list[:10])
for i in range(0, -1, -1):
    print(prime_list[i])
    out = un_shift(out, prime_list[i])
    out = rot(out, prime_list[i])

print(out)
