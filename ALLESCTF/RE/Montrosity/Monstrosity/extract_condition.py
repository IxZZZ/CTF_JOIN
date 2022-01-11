file = open('condition.txt', 'r')
arr_condition = []
count = 0

strs = file.read()
arr_sub = []
for line in strs.split('\t\n'):
    if count == 10:
        arr_condition.append(arr_sub)
        arr_sub = []
        count = 0
    i = int(line[1])
    j = int(line[4])
    print(i, j)
    condition = line[7:]
    arr_sub.append(condition.strip('\t\n'))
    count += 1

    # print(arr[i][j])
arr_condition.append(arr_sub)
print(arr_condition)