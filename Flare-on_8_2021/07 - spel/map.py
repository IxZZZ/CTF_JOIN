base = 424
arr = [436,437,430,432,431,430,429,425,424,427,428,441,439,444,443,445,426,434,440,435,438,426]
print(len(arr))
str = 'l3rlcps_7r_vb33eehskc3'

res = ''

for i in arr:
    res+=str[i-base]

print(res+'@')