with open('expression.txt','r') as file:
    str = file.read()
    for s in str.split('&'):
        print()