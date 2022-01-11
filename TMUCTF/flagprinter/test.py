limit = 37 ** 2 + 1

def count_v3(a1):
	v3 = 0
	for i in range(1, a1):
		v3 = (a1 + (v3 ^ i)) % 10
	return v3

v3 = []
for i in range(limit):
	v3.append(count_v3(i))

result = []
for i in range(limit):
	if i == 0:
		result.append(0)
	elif i == 1:
		result.append(10)
	else:
		result.append((i + v3[i] * (result[i - 1] + result[i - 2])) % 1000000)
res = []
for i in range(37+1):
	index = i*i
	print('v3: ' + str(v3[index]))
	print('result: ' + str(result[index]))
	res.append(result[index])

print(res)
