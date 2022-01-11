arr = [158, 191, 174, 185, 82, 116, 29, 2, 42, 53, 97, 102, 80, 88,
       82, 4, 87, 36, 99, 115, 158, 134, 81, 123, 23, 28, 62, 34, 99, 115]

f = open('flag.jpeg','rb')

s = f.read()[:len(arr)]

for i in range(len(arr)):
    print(chr(arr[i]^s[i]),end='')
