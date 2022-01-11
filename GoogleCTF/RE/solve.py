def define_func(parts,var):
    var[parts[1]] = int(parts[2])


def if_func(parts,var):
    if parts[2] == '==':
        return var[parts[1]] == int(parts[3])
    elif parts[2] == '>':
        return var[parts[1]] > int(parts[3])
    elif  parts[2] == '<':
        return var[parts[1]] < int(parts[3])
    elif  parts[2] == '>=':
        return var[parts[1]] >= int(parts[3])
    else:
        return var[parts[1]] <=int(parts[3])



def ifdef_func(parts,var):
    for key in var:
        if key == parts[1]:
            return True
    
    return False


def ifndef_func(parts, var):
    if ifdef_func(parts,var) == True:
        return False
    else:
        return True

def undef_func(parts,var):
    var.pop(parts[1])


def error_func(parts,var):
    print(parts[1])

def include_func(parts,var):
    print(parts[1])

def else_func(parts,var):
    return 2
    
number_flow = {'#define': 0, '#if': 1, '#endif': 2, '#ifndef': 3, '#undef': 4,
    '#error': 5, '#ifdef': 6, '#include': 7, '#else': 8}

file = open('code.txt','r').read()

lines = file.split('\n')
var = {'S':0}

continue_to_else = False
endif_count = 0
for line in lines:
    parts = line.split(' ')
    if continue_to_else == True and number_flow[parts[0]] != 8:
        continue
    if number_flow[parts[0]] == 1:
        endif_count+=1
        condition = if_func(parts,var)
        if condition == True:
            continue
        else:
            continue_to_else = True
    elif number_flow[parts[0]] == 0:
        define_func(parts,var)
        continue
    elif  number_flow[parts[0]] == 2:
        endif_count-= 1
    elif  number_flow[parts[0]] == 3:
        
