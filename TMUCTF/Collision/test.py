arr = []

len_n = 5
for i in range(len_n):
    arr.append(pow(31,i,10000000))

print(arr)

str = 'A'*len_n
arr = arr[::-1]
a = 0
for i in range(len(str)):
    a += ord(str[i])*arr[i]

print(a)