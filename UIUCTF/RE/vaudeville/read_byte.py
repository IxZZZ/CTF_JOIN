f = open('/tmp/tmp_12345', 'rb')

bytes = f.read()

for i in bytes:
    print(hex(i),end=' ')
