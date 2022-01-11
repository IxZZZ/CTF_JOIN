import pickletools

with open('rick.pickle','rb') as file:
    str_b = file.read()
    code = pickletools.dis(str_b)
    tup = []
    for op in pickletools.genops(code):
        (opcode, arg, pos) = op
        if (opcode.name == "INT"):
            tup.append(arg)
    pickletools.dis(bytes(tup))
