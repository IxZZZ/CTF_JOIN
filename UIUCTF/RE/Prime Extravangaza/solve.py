import hashlib
s = 0
for i in range(0,5,1):
    s += 19753*(i+1)

print(hashlib.md5(str(s).encode()).hexdigest())