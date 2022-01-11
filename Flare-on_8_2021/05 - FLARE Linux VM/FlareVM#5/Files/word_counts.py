count = {}
with open('Quijote.txt', 'r') as file:
    f = file.read().strip('\n').strip('.')
    str = f.split(' ')
    for i in range(len(str)):
        str[i] = str[i].strip(',')
        str[i] = str[i].strip('.')
    set_a = list(str)
    for w in str:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1

unique = 0
for key in count:
    if count[key] == 1:
        unique += 1

print(count)
print(unique)
