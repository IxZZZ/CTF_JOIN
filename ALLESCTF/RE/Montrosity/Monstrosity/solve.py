

def extract(str):
    i, j = str[:3].split('_')
    return int(i), int(j)


file = open('data.txt', 'r')


arr_strs = []

is_start = True
arr_next_step = []
character = ''
isValid = True
# count = 82
for line in file.readlines():
    # if count == 0:
    #     break
    if 'private static void visitField' in line:
        if len(arr_next_step) != 0:
            arr_strs.append(arr_next_step)
        index = line.find('visitField') + 11
        arr_next_step = []
        arr_next_step.append(line[index:index+3])
        isValid = True
    elif 'bool flag' in line:
        index = line.find("'")+1
        character = line[index:index+1]
        isValid = True
    elif 'MazeWalker.outOfBounds' in line:
        character = ''
        isValid = True
    elif 'MazeWalker.isValid' in line:
        isValid = False
    elif ('MazeWalker.visitField' in line) and isValid == True:
        if character == '':
            print('Wrong')
        index = line.find('visitField') + 11
        step = line[index:index+3] + '_' + character
        arr_next_step.append(step)
        character = ''
        isValid = True
    # count -= 1

# print(arr_next_step)
# print(arr_strs)


def find(arr_strs, find_pos):
    all_step = []
    for pos in arr_strs:
        for step in pos:
            if step[:4] == find_pos + '_':
                all_step.append(pos[0] + '_' + step[4])

    return all_step


def check(point, point2):
    arr_condition = [['Top | Left | Visited', 'Right | Left | Visited', 'Right | Left | Visited', 'Right | Left | Visited', 'Right | Left | Visited', 'Right | Left | Visited', 'Bottom | Left | Visited', 'Top | Left | Visited', 'Right | Left | Visited', 'Right | Bottom | Left | Visited'], ['Top | Right | Visited', 'Right | Left | Visited', 'Bottom | Left | Visited', 'Top | Bottom | Left | Visited', 'Top | Left | Visited', 'Right | Left | Visited', 'Right | Bottom | Visited', 'Top | Visited', 'Right | Left | Visited', 'Bottom | Left | Visited'], ['Top | Left | Visited', 'Right | Bottom | Left | Visited', 'Top | Bottom | Visited', 'Top | Bottom | Visited', 'Top | Right | Visited', 'Right | Left | Visited', 'Bottom | Left | Visited', 'Top | Right | Visited', 'Right | Bottom | Left | Visited', 'Top | Bottom | Visited'], ['Top | Right | Visited', 'Right | Left | Visited', 'Right | Bottom | Visited', 'Top | Bottom | Visited', 'Top | Left | Visited', 'Bottom | Left | Visited', 'Top | Right | Visited', 'Bottom | Left | Visited', 'Top | Left | Visited', 'Right | Bottom | Visited'], ['Top | Left | Visited', 'Left | Visited', 'Right | Left | Visited', 'Right | Bottom | Visited', 'Top | Bottom | Visited', 'Top | Bottom | Visited', 'Top | Left | Visited', 'Right | Bottom | Visited', 'Top | Visited', 'Bottom | Left | Visited'], [
        'Top | Bottom | Visited', 'Top | Bottom | Visited', 'Top | Left | Visited', 'Right | Left | Visited', 'Right | Bottom | Visited', 'Top | Bottom | Visited', 'Top | Bottom | Visited', 'Top | Bottom | Left | Visited', 'Top | Bottom | Visited', 'Top | Bottom | Visited'], ['Top | Bottom | Visited', 'Top | Right | Visited', 'Right | Bottom | Visited', 'Top | Right | Left | Visited', 'Bottom | Left | Visited', 'Top | Bottom | Visited', 'Top | Bottom | Visited', 'Top | Visited', 'Right | Bottom | Visited', 'Top | Bottom | Visited'], ['Top | Right | Visited', 'Right | Left | Visited', 'Right | Left | Visited', 'Bottom | Left | Visited', 'Top | Bottom | Visited', 'Top | Right | Visited', 'Right | Bottom | Visited', 'Top | Right | Visited', 'Right | Bottom | Left | Visited', 'Top | Bottom | Visited'], ['Top | Left | Visited', 'Right | Left | Visited', 'Bottom | Left | Visited', 'Top | Right | Visited', 'Right | Visited', 'Bottom | Left | Visited', 'Top | Left | Visited', 'Bottom | Left | Visited', 'Top | Left | Visited', 'Bottom | Visited'], ['Top | Right | Visited', 'Right | Bottom | Left | Visited', 'Top | Right | Visited', 'Right | Left | Visited', 'Right | Left | Visited', 'Right | Visited', 'Right | Bottom | Visited', 'Top | Right | Visited', 'Right | Bottom | Visited', 'Top | Right | Bottom | Visited']]
    edge = 'Right'
    if point[0] < point2[0]:
        edge = 'Left'
    if point[1] > point2[1]:
        edge = 'Bottom'
    if point[1] < point2[1]:
        edge = 'Top'

    if edge in arr_condition[point2[0]][point2[1]]:
        return False
    else:
        return True

def recur(arr_strs, current_step, path):
    if (current_step == '0_0'):
        print(path)
        return
    for pos in find(arr_strs, current_step):
        path += pos[4]
        point = list(extract(current_step+'_'))
        point2 = list(extract(pos+'_'))
        print(point,point2)
        if check(point, point2):
            recur(arr_strs, pos[:3], path)



# str_path = ''
# current_pos = '9_9'
# while current_pos != '0_0':
#     find_alls = find(arr_strs,current_pos)
#     print(find_alls)
#     break

# recur(arr_strs,'9_9','')

# print(find(arr_strs,'1_0'))


# step = 0
# while step >= len(str):
#     for
print(find(arr_strs, '9_8'))
print(arr_strs)
# recur(arr_strs,'9_8','')

# print(check([9,8],[9,7]))
# print(check([9,7],[9,6]))