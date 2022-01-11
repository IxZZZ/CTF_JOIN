with open('./save/instant_noodles.txt.broken', 'rb') as f:
    str = f.read()

    for i in str:
        if i != 0:
            print(chr(i-4),end='')
