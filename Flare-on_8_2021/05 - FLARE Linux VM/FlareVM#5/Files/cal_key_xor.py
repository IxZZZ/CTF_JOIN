with open('unagi.txt.broken', 'rb') as file:
    key = file.read()[0x26:]
    
    # key = missing+key
    
    str = b'/\n[U]don noodles\n[S]trawberries\n[R]ees'

    f = open('shopping_list.txt.broken','rb')

    head = f.read()[:38]

    missing = b''
    for i in range(0x26):
        missing += bytes([head[i]^str[i]])
    # missing = b'\x00'*38
    key = missing+key
    print(key)

    with open('key.txt','wb') as file_key:
        file_key.write(key)
