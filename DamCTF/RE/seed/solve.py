import sys
import time
import random
import hashlib


def hash(text):
    return hashlib.sha256(str(text).encode()).hexdigest()

def print_from_seed(s):
    arr = []
    while True:
        random.seed(s, version=2)

        x = random.random()

        if x not in arr:
            arr.append(x)
            print(arr)
        if len(arr) == 17:
            break
        s = s+1
    print(arr[16])

    print(hash(arr[16]))


arr_res = [0.3322089622063289, 0.10859805708337256, 0.39751456956943265, 0.6194981263678604, 0.32054505821893853, 0.2674908181379442, 0.5379388350878211, 0.7799698997586163,
           0.6893538761284775, 0.7171513961367021, 0.29362186264112344, 0.06571100672753238, 0.9607588522085679, 0.33534977507836194, 0.07384192274198853, 0.1448081453121044]

print(len(arr_res))

# arr = []
# s = round(time.time())

# while True:
#     random.seed(s, version=2)

#     x = random.random()

#     if x==arr_res[0]:
#         print(s)
#         break
#     s -= 1

print_from_seed(1634187271)

