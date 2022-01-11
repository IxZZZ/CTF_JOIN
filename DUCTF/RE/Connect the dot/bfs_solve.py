def bfs(x_first, y_first, x_des, y_des, can_go):
    save = [['' for i in range(60)] for j in range(60)]
    best = [[[] for i in range(60)] for j in range(60)]
    que = []
    i = 0
    que.append([x_first, y_first])
    save[x_first][y_first] = '.'
    while i < len(que):
        x, y = que[i][0], que[i][1]
        if x == x_des and y == y_des:
            path = ''
            while x != x_first or y != y_first:
                path += save[x][y]
                x, y = best[x][y]
            return path[::-1]
            break
        for go in can_go[x][y]:
            if save[go[0]][go[1]] == '':
                que.append([go[0], go[1]])
                save[go[0]][go[1]] = go[2]
                best[go[0]][go[1]] = [x, y]
        i += 1

arr_maze = [[11, 10, 12, 9, 10, 10, 8, 8, 10, 14, 9, 8, 10, 10, 12, 11, 8, 10, 12, 9, 10, 12, 9, 10, 10, 10, 12, 11, 10, 10, 10, 8, 12, 9, 8, 14, 9, 10, 12, 9, 8, 12, 11, 10, 10, 10, 8, 12, 11, 8, 10, 10, 8, 14, 9, 12, 9, 8, 12, 13], [13, 9, 6, 5, 9, 12, 5, 7, 9, 12, 5, 5, 9, 12, 3, 10, 6, 9, 6, 5, 9, 6, 3, 12, 9, 14, 3, 10, 10, 10, 12, 7, 1, 6, 3, 12, 3, 12, 5, 5, 5, 3, 10, 10, 10, 10, 6, 3, 12, 5, 9, 12, 7, 9, 6, 5, 5, 5, 3, 4], [5, 5, 11, 2, 6, 5, 3, 10, 6, 5, 5, 3, 6, 3, 10, 10, 12, 5, 9, 6, 3, 12, 9, 6, 1, 10, 10, 10, 8, 14, 3, 12, 3, 12, 13, 5, 9, 6, 3, 6, 5, 9, 10, 10, 10, 10, 12, 9, 6, 5, 5, 3, 10, 2, 12, 3, 6, 5, 9, 6], [5, 3, 12, 11, 12, 1, 14, 9, 12, 3, 6, 9, 12, 9, 10, 12, 5, 3, 6, 13, 9, 6, 5, 11, 2, 10, 12, 13, 3, 10, 10, 6, 11, 2, 6, 5, 3, 10, 12, 9, 6, 5, 11, 12, 9, 10, 6, 5, 11, 0, 2, 14, 9, 12, 3, 10, 14, 5, 5, 13], [1, 12, 3, 12, 3, 6, 9, 6, 3, 10, 12, 5, 3, 6, 13, 3, 6, 9, 10, 6, 5, 11, 2, 10, 12, 13, 3, 2, 10, 10, 12, 9, 10, 10, 12, 3, 8, 10, 6, 3, 12, 3, 8, 6, 3, 10, 12, 3, 12, 5, 9, 10, 6, 3, 10, 10, 10, 6, 5, 5], [5, 3, 12, 3, 10, 12, 3, 12, 9, 10, 6, 1, 12, 11, 2, 8, 12, 1, 10, 12, 3, 12, 9, 10, 6, 5, 9, 8, 8, 14, 5, 1, 10, 12, 3, 12, 3, 10, 12, 13, 5, 9, 6, 9, 10, 12, 1, 12, 5, 7, 5, 9, 14, 9, 8, 14, 9, 10, 6, 5], [1, 12, 3, 10, 12, 5, 9, 6, 3, 12, 11, 6, 5, 9, 12, 7, 1, 6, 9, 6, 9, 6, 5, 9, 14, 1, 6, 5, 5, 9, 6, 3, 12, 3, 12, 5, 11, 10, 2, 4, 5, 3, 12, 5, 11, 2, 6, 7, 5, 9, 6, 1, 10, 6, 5, 9, 2, 10, 10, 6], [5, 5, 9, 12, 7, 5, 3, 10, 12, 3, 10, 10, 6, 5, 3, 12, 5, 13, 5, 9, 6, 9, 6, 3, 8, 6, 9, 6, 7, 3, 10, 12, 3, 12, 5, 3, 12, 9, 12, 5, 3, 12, 5, 3, 10, 10, 10, 10, 6, 3, 12, 5, 9, 12, 3, 6, 9, 10, 10, 12], [5, 5, 5, 3, 10, 6, 9, 10, 6, 9, 10, 10, 10, 6, 9, 6, 5, 5, 5, 3, 12, 3, 10, 12, 3, 12, 3, 10, 12, 9, 10, 6, 9, 6, 5, 9, 2, 6, 5, 3, 12, 5, 5, 9, 10, 12, 9, 10, 10, 8, 6, 3, 6, 5, 9, 10, 6, 9, 12, 5], [5, 5, 5, 9, 10, 12, 5, 9, 10, 4, 9, 10, 12, 13, 3, 12, 3, 6, 1, 12, 3, 10, 10, 6, 13, 5, 11, 12, 5, 3, 10, 12, 7, 9, 4, 7, 9, 12, 3, 12, 7, 5, 5, 3, 14, 1, 6, 9, 10, 6, 9, 12, 13, 5, 3, 12, 11, 6, 5, 5], [5, 5, 3, 6, 13, 3, 6, 5, 13, 3, 6, 13, 5, 3, 10, 2, 10, 10, 6, 3, 10, 10, 12, 11, 4, 5, 9, 4, 1, 10, 14, 3, 12, 5, 7, 9, 6, 5, 13, 3, 10, 6, 3, 10, 12, 3, 14, 3, 10, 12, 5, 5, 3, 4, 9, 2, 10, 8, 6, 5], [7, 5, 9, 10, 2, 10, 12, 3, 4, 11, 8, 4, 3, 10, 10, 140, 11, 10, 10, 12, 9, 12, 1, 10, 6, 5, 5, 5, 3, 10, 12, 9, 6, 3, 10, 2, 14, 5, 1, 10, 10, 8, 10, 14, 3, 10, 10, 10, 12, 3, 4, 3, 12, 5, 5, 9, 12, 7, 9, 4], [9, 6, 5, 13, 9, 10, 4, 13, 5, 9, 6, 5, 11, 10, 12, 3, 10, 10, 12, 3, 4, 5, 5, 9, 10, 6, 5, 5, 9, 10, 4, 3, 12, 9, 10, 12, 9, 6, 5, 13, 9, 4, 9, 10, 10, 10, 8, 12, 3, 12, 3, 14, 5, 5, 5, 5, 3, 10, 6, 5], [5, 9, 6, 5, 3, 12, 3, 6, 3, 6, 13, 3, 10, 12, 1, 8, 10, 12, 3, 12, 7, 3, 6, 5, 11, 8, 6, 5, 5, 11, 4, 13, 3, 6, 13, 3, 6, 13, 3, 4, 5, 5, 3, 8, 10, 14, 5, 3, 14, 5, 9, 10, 6, 7, 5, 5, 11, 12, 9, 6], [1, 6, 11, 0, 12, 3, 10, 8, 12, 13, 1, 10, 12, 5, 5, 5, 11, 6, 9, 6, 9, 10, 10, 6, 9, 6, 13, 5, 3, 12, 3, 2, 10, 10, 2, 10, 12, 3, 10, 6, 5, 7, 9, 6, 9, 12, 5, 9, 10, 6, 1, 12, 9, 10, 6, 3, 12, 3, 4, 13], [3, 10, 12, 5, 3, 14, 9, 6, 3, 4, 5, 13, 3, 6, 5, 5, 9, 8, 6, 9, 6, 9, 10, 10, 6, 9, 6, 5, 9, 6, 9, 10, 10, 8, 10, 14, 3, 10, 10, 10, 4, 9, 6, 13, 5, 1, 6, 5, 9, 10, 6, 5, 5, 11, 8, 12, 3, 12, 3, 6], [13, 9, 6, 3, 10, 12, 5, 9, 14, 5, 5, 3, 10, 10, 6, 5, 5, 7, 9, 6, 9, 4, 9, 14, 9, 2, 10, 6, 5, 11, 2, 12, 11, 6, 9, 10, 10, 10, 10, 10, 6, 3, 12, 5, 5, 5, 9, 6, 3, 12, 9, 6, 5, 9, 6, 3, 12, 5, 9, 12], [5, 5, 11, 8, 12, 5, 5, 1, 10, 6, 3, 10, 10, 10, 12, 5, 3, 10, 6, 13, 5, 5, 3, 12, 5, 9, 10, 12, 3, 10, 12, 5, 9, 12, 5, 11, 10, 8, 12, 11, 8, 14, 5, 5, 5, 7, 5, 9, 10, 6, 3, 10, 2, 6, 9, 14, 5, 3, 6, 5], [1, 2, 10, 6, 5, 5, 5, 3, 10, 12, 9, 14, 9, 10, 6, 1, 10, 12, 9, 2, 6, 5, 9, 6, 3, 6, 9, 6, 13, 9, 6, 5, 5, 3, 2, 10, 8, 6, 3, 10, 4, 9, 6, 5, 3, 12, 5, 3, 12, 9, 10, 12, 9, 12, 3, 12, 5, 9, 14, 5], [5, 13, 9, 12, 5, 5, 5, 9, 12, 5, 3, 12, 3, 10, 10, 6, 13, 5, 3, 12, 9, 6, 3, 10, 10, 12, 5, 9, 6, 5, 9, 2, 6, 9, 10, 12, 7, 9, 12, 9, 6, 3, 10, 2, 12, 3, 6, 11, 4, 3, 14, 5, 5, 3, 12, 3, 2, 6, 9, 4], [3, 4, 5, 5, 3, 6, 3, 6, 5, 3, 10, 4, 9, 10, 8, 14, 1, 6, 13, 5, 3, 10, 12, 9, 12, 5, 3, 4, 9, 6, 3, 10, 12, 3, 12, 147, 10, 6, 5, 7, 9, 10, 8, 12, 3, 10, 10, 12, 3, 8, 10, 6, 5, 13, 5, 9, 10, 10, 6, 5], [9, 6, 5, 3, 8, 10, 10, 12, 5, 11, 12, 5, 3, 14, 5, 9, 6, 9, 4, 3, 12, 13, 3, 6, 5, 5, 9, 6, 3, 12, 9, 12, 5, 13, 5, 9, 10, 14, 5, 9, 6, 9, 6, 5, 9, 12, 13, 5, 11, 4, 9, 10, 4, 3, 2, 6, 9, 12, 9, 6], [3, 12, 3, 12, 7, 9, 12, 3, 6, 9, 6, 3, 10, 8, 6, 3, 12, 5, 3, 12, 5, 1, 12, 9, 6, 5, 3, 10, 12, 3, 6, 5, 3, 6, 5, 1, 10, 12, 3, 6, 13, 3, 12, 5, 5, 3, 6, 3, 12, 7, 3, 12, 7, 9, 10, 12, 7, 1, 6, 13], [13, 5, 13, 3, 10, 6, 5, 13, 9, 2, 8, 14, 9, 6, 9, 10, 6, 3, 12, 5, 3, 4, 7, 5, 9, 2, 10, 10, 4, 9, 8, 6, 9, 10, 6, 3, 12, 3, 12, 9, 2, 12, 5, 3, 6, 9, 10, 12, 5, 9, 10, 6, 9, 2, 14, 1, 12, 3, 10, 4], [5, 3, 2, 12, 9, 12, 5, 5, 1, 14, 3, 10, 2, 12, 3, 12, 11, 10, 164, 1, 12, 5, 9, 6, 5, 9, 10, 12, 7, 5, 7, 9, 6, 9, 10, 10, 6, 13, 3, 2, 14, 5, 5, 9, 12, 5, 13, 3, 6, 5, 9, 10, 6, 9, 12, 7, 5, 11, 12, 5], [1, 8, 14, 3, 6, 5, 5, 3, 6, 9, 12, 9, 12, 5, 13, 3, 10, 12, 7, 5, 7, 5, 3, 12, 7, 3, 12, 3, 12, 3, 12, 3, 12, 1, 10, 10, 10, 2, 10, 14, 9, 6, 3, 6, 3, 6, 1, 8, 10, 6, 3, 12, 9, 6, 3, 10, 6, 9, 6, 5], [7, 5, 9, 10, 12, 5, 3, 10, 10, 6, 3, 6, 5, 3, 4, 11, 12, 3, 12, 5, 9, 6, 13, 3, 8, 14, 1, 14, 3, 12, 3, 12, 5, 7, 9, 10, 10, 12, 9, 12, 5, 9, 10, 8, 12, 13, 5, 3, 12, 9, 10, 6, 5, 9, 10, 10, 8, 4, 9, 6], [9, 6, 3, 12, 3, 6, 9, 12, 9, 10, 10, 10, 6, 13, 3, 10, 4, 9, 6, 3, 2, 12, 1, 12, 3, 10, 6, 9, 10, 2, 12, 5, 3, 12, 5, 9, 14, 3, 6, 5, 3, 2, 14, 5, 5, 1, 6, 13, 3, 2, 10, 14, 5, 3, 14, 9, 6, 5, 5, 13], [1, 10, 12, 5, 11, 10, 4, 5, 3, 10, 12, 11, 8, 2, 10, 10, 6, 3, 10, 12, 13, 5, 5, 5, 11, 8, 14, 5, 13, 9, 6, 1, 12, 3, 6, 5, 9, 10, 12, 5, 9, 10, 10, 6, 5, 3, 10, 2, 12, 9, 10, 10, 6, 9, 188, 5, 11, 4, 5, 5], [1, 14, 3, 4, 9, 10, 6, 5, 9, 14, 3, 12, 3, 10, 10, 12, 11, 12, 9, 6, 3, 2, 6, 3, 12, 5, 9, 6, 5, 3, 12, 5, 5, 11, 10, 2, 2, 14, 5, 5, 5, 9, 12, 13, 3, 12, 11, 10, 6, 5, 9, 10, 10, 4, 5, 3, 12, 5, 3, 4], [7, 9, 12, 3, 6, 11, 12, 5, 5, 9, 12, 5, 13, 9, 10, 6, 9, 6, 3, 12, 9, 10, 10, 12, 5, 5, 3, 12, 1, 10, 6, 5, 3, 10, 10, 10, 10, 12, 5, 3, 6, 5, 3, 2, 12, 5, 9, 10, 10, 6, 1, 10, 14, 5, 3, 10, 4, 3, 14, 5], [9, 6, 3, 12, 9, 8, 6, 3, 4, 5, 5, 5, 5, 5, 11, 8, 2, 8, 14, 3, 6, 11, 12, 5, 3, 0, 14, 5, 3, 10, 12, 5, 9, 10, 10, 12, 11, 2, 2, 8, 10, 6, 9, 12, 7, 5, 1, 12, 11, 10, 6, 9, 12, 5, 9, 12, 5, 9, 10, 6], [5, 11, 10, 4, 7, 3, 10, 10, 6, 5, 3, 6, 5, 3, 12, 5, 13, 3, 8, 10, 8, 10, 6, 3, 12, 7, 9, 6, 9, 10, 6, 3, 6, 9, 10, 4, 9, 10, 12, 7, 9, 10, 6, 3, 10, 6, 7, 1, 10, 10, 12, 5, 5, 5, 5, 3, 6, 3, 12, 13], [5, 9, 12, 5, 9, 10, 10, 10, 10, 6, 11, 12, 1, 10, 6, 5, 1, 14, 3, 12, 7, 9, 8, 14, 5, 9, 6, 11, 2, 10, 10, 12, 13, 5, 11, 4, 5, 13, 3, 10, 6, 11, 10, 10, 8, 10, 12, 3, 14, 9, 6, 5, 5, 5, 3, 10, 8, 14, 5, 5], [5, 5, 5, 3, 6, 9, 12, 11, 10, 8, 10, 6, 3, 12, 13, 5, 3, 8, 14, 3, 12, 5, 3, 12, 5, 3, 10, 10, 12, 9, 12, 3, 4, 3, 12, 5, 3, 2, 12, 11, 8, 10, 12, 9, 6, 9, 6, 9, 10, 6, 9, 6, 3, 6, 9, 12, 7, 9, 6, 5], [5, 5, 3, 10, 10, 6, 3, 10, 12, 1, 12, 201, 10, 6, 3, 2, 10, 6, 9, 10, 4, 5, 13, 3, 6, 9, 10, 12, 5, 5, 5, 9, 6, 9, 6, 3, 12, 13, 3, 10, 6, 13, 3, 6, 9, 6, 11, 2, 12, 9, 4, 9, 10, 10, 6, 3, 10, 6, 9, 6], [5, 3, 10, 12, 9, 10, 10, 12, 5, 7, 3, 2, 10, 12, 9, 10, 10, 12, 3, 12, 5, 3, 4, 11, 10, 4, 9, 2, 6, 5, 3, 6, 13, 5, 11, 10, 2, 2, 10, 10, 8, 6, 9, 10, 6, 11, 8, 12, 5, 5, 7, 5, 9, 10, 10, 14, 9, 10, 2, 12], [3, 8, 12, 3, 6, 11, 12, 5, 3, 10, 12, 9, 12, 3, 4, 9, 12, 3, 10, 6, 5, 13, 3, 12, 9, 4, 7, 9, 12, 5, 9, 10, 6, 3, 8, 12, 9, 10, 12, 9, 6, 9, 6, 11, 8, 10, 6, 3, 6, 3, 12, 5, 3, 8, 10, 12, 3, 12, 9, 4], [9, 6, 3, 14, 9, 8, 6, 1, 10, 14, 1, 6, 5, 11, 6, 5, 5, 9, 12, 9, 6, 1, 12, 3, 6, 5, 9, 6, 5, 3, 6, 9, 10, 12, 7, 5, 3, 12, 3, 6, 13, 5, 11, 8, 6, 11, 10, 10, 8, 10, 4, 3, 12, 3, 14, 3, 10, 6, 5, 5], [5, 9, 12, 9, 6, 3, 10, 6, 9, 12, 3, 14, 1, 12, 9, 6, 5, 7, 3, 2, 10, 6, 5, 13, 9, 6, 5, 11, 2, 10, 10, 4, 11, 2, 218, 6, 13, 5, 9, 10, 4, 3, 10, 6, 9, 10, 10, 10, 6, 9, 6, 13, 3, 10, 10, 10, 10, 10, 6, 5], [1, 6, 5, 3, 12, 13, 9, 10, 6, 3, 10, 12, 7, 3, 2, 14, 1, 10, 10, 10, 10, 12, 3, 4, 5, 13, 3, 10, 10, 10, 12, 7, 9, 10, 10, 12, 3, 2, 6, 13, 3, 12, 9, 12, 5, 9, 8, 10, 12, 5, 9, 2, 10, 8, 8, 10, 10, 10, 14, 5], [3, 14, 1, 12, 5, 5, 5, 9, 12, 9, 14, 5, 9, 10, 10, 12, 7, 9, 12, 9, 12, 3, 12, 7, 3, 4, 9, 10, 14, 9, 6, 9, 6, 9, 14, 3, 12, 9, 8, 0, 14, 5, 5, 3, 6, 5, 3, 12, 5, 5, 7, 9, 12, 7, 5, 9, 10, 12, 9, 6], [9, 8, 6, 7, 3, 4, 3, 6, 5, 1, 12, 1, 6, 11, 8, 2, 10, 6, 3, 6, 3, 12, 3, 12, 9, 6, 3, 12, 9, 6, 9, 6, 11, 2, 8, 12, 5, 7, 5, 7, 9, 6, 1, 10, 12, 3, 12, 5, 7, 3, 10, 6, 3, 12, 1, 6, 9, 6, 5, 13], [5, 7, 9, 12, 9, 2, 14, 9, 6, 5, 3, 6, 9, 12, 5, 9, 10, 12, 9, 10, 14, 5, 9, 6, 3, 10, 10, 4, 5, 9, 6, 9, 10, 10, 6, 5, 3, 12, 3, 10, 2, 12, 3, 14, 3, 12, 7, 5, 9, 10, 12, 9, 12, 5, 7, 9, 6, 9, 6, 5], [3, 10, 6, 3, 2, 14, 9, 6, 13, 5, 13, 9, 6, 5, 7, 5, 13, 5, 5, 9, 10, 6, 1, 10, 10, 8, 14, 5, 5, 3, 12, 5, 9, 10, 14, 5, 13, 3, 10, 12, 11, 2, 12, 9, 10, 6, 9, 6, 5, 13, 3, 6, 5, 3, 10, 4, 9, 6, 9, 4], [9, 10, 10, 10, 10, 12, 1, 12, 3, 2, 6, 1, 14, 5, 9, 2, 6, 5, 5, 3, 12, 11, 0, 10, 14, 5, 9, 6, 3, 12, 3, 6, 3, 12, 9, 6, 3, 8, 12, 5, 9, 12, 5, 5, 9, 10, 2, 10, 6, 3, 8, 14, 3, 10, 12, 5, 5, 11, 4, 5], [5, 11, 8, 10, 10, 6, 5, 3, 10, 10, 10, 6, 9, 4, 1, 14, 9, 6, 1, 14, 3, 12, 7, 9, 10, 4, 5, 9, 14, 3, 10, 8, 10, 6, 3, 12, 9, 6, 5, 3, 6, 5, 1, 6, 3, 10, 10, 12, 9, 10, 6, 9, 8, 14, 3, 6, 3, 12, 5, 5], [1, 12, 3, 10, 12, 11, 2, 10, 10, 14, 9, 8, 6, 7, 5, 9, 6, 11, 2, 10, 10, 2, 10, 6, 11, 6, 5, 5, 9, 10, 12, 3, 10, 10, 12, 3, 6, 9, 6, 13, 9, 6, 7, 9, 12, 9, 12, 5, 3, 10, 10, 4, 3, 10, 12, 9, 10, 6, 5, 7], [7, 5, 9, 12, 5, 9, 10, 12, 9, 10, 6, 5, 9, 10, 6, 3, 10, 10, 12, 9, 10, 12, 9, 12, 9, 12, 5, 5, 5, 13, 3, 12, 9, 12, 5, 9, 12, 3, 10, 4, 3, 10, 10, 6, 5, 5, 5, 3, 10, 10, 12, 7, 9, 10, 6, 3, 10, 236, 3, 12], [9, 6, 5, 7, 5, 5, 13, 3, 6, 9, 14, 5, 3, 12, 9, 10, 10, 12, 3, 6, 9, 6, 5, 3, 6, 3, 6, 1, 2, 6, 9, 6, 5, 5, 3, 6, 1, 10, 14, 5, 9, 10, 12, 9, 6, 7, 3, 8, 10, 12, 3, 8, 6, 9, 10, 10, 12, 3, 12, 5], [1, 12, 3, 8, 6, 5, 1, 10, 14, 1, 10, 2, 14, 5, 5, 9, 12, 3, 10, 12, 3, 10, 6, 11, 10, 8, 12, 7, 9, 12, 5, 9, 6, 3, 12, 9, 6, 9, 12, 3, 6, 13, 5, 3, 12, 9, 12, 5, 9, 4, 9, 6, 9, 6, 9, 12, 1, 14, 5, 5], [5, 3, 12, 3, 12, 5, 3, 8, 10, 6, 9, 10, 10, 6, 3, 6, 3, 12, 13, 5, 9, 10, 10, 8, 10, 6, 3, 10, 6, 5, 5, 3, 12, 11, 2, 6, 9, 6, 3, 10, 10, 4, 3, 12, 5, 5, 5, 7, 5, 7, 5, 9, 2, 14, 5, 5, 3, 12, 5, 5], [1, 14, 5, 13, 5, 3, 12, 5, 9, 10, 6, 11, 10, 8, 10, 12, 11, 2, 6, 5, 5, 9, 10, 6, 11, 10, 8, 14, 9, 6, 1, 12, 3, 10, 12, 9, 6, 9, 8, 10, 12, 3, 12, 5, 3, 6, 3, 12, 5, 9, 6, 5, 13, 9, 6, 3, 10, 6, 3, 4], [5, 9, 6, 3, 0, 10, 6, 7, 5, 9, 10, 10, 10, 6, 13, 3, 12, 9, 12, 3, 6, 5, 9, 8, 10, 12, 3, 12, 3, 12, 5, 3, 10, 14, 3, 6, 9, 6, 5, 13, 3, 12, 5, 3, 12, 9, 12, 5, 3, 6, 9, 6, 5, 3, 10, 10, 10, 10, 10, 6], [5, 3, 10, 12, 7, 9, 10, 10, 6, 3, 12, 9, 8, 12, 3, 12, 5, 5, 3, 12, 9, 6, 5, 5, 11, 2, 10, 4, 13, 5, 5, 9, 10, 10, 10, 10, 6, 9, 6, 5, 9, 6, 1, 12, 5, 7, 5, 3, 10, 10, 6, 9, 4, 9, 8, 14, 9, 8, 12, 13], [3, 12, 9, 6, 9, 6, 13, 9, 8, 10, 6, 7, 5, 3, 10, 4, 5, 3, 12, 5, 5, 11, 4, 3, 12, 9, 10, 2, 6, 5, 5, 3, 8, 14, 9, 10, 10, 6, 9, 2, 6, 9, 6, 5, 3, 12, 1, 8, 10, 10, 10, 6, 5, 5, 3, 10, 6, 5, 5, 5], [9, 6, 3, 12, 5, 9, 6, 5, 5, 9, 10, 12, 5, 9, 12, 7, 3, 10, 6, 5, 1, 12, 5, 9, 6, 7, 9, 12, 9, 6, 1, 10, 6, 9, 6, 9, 12, 13, 5, 11, 12, 5, 13, 3, 12, 5, 7, 1, 12, 9, 12, 9, 6, 3, 14, 9, 12, 5, 3, 4], [3, 12, 9, 4, 5, 3, 10, 6, 3, 2, 14, 5, 5, 5, 3, 8, 12, 13, 9, 6, 7, 5, 5, 3, 10, 12, 5, 3, 6, 11, 2, 10, 14, 5, 11, 4, 5, 5, 5, 9, 4, 5, 3, 10, 6, 3, 12, 7, 3, 4, 5, 3, 10, 12, 9, 6, 5, 5, 9, 6], [9, 6, 5, 7, 3, 12, 9, 10, 10, 12, 9, 6, 1, 6, 9, 6, 3, 6, 3, 10, 12, 5, 5, 13, 9, 6, 3, 10, 10, 10, 12, 9, 10, 6, 9, 6, 3, 6, 3, 6, 5, 3, 12, 9, 10, 12, 3, 10, 12, 7, 3, 12, 13, 5, 5, 9, 6, 5, 3, 12], [3, 14, 3, 10, 10, 2, 6, 11, 10, 2, 6, 11, 2, 14, 3, 10, 10, 10, 10, 10, 2, 6, 3, 6, 3, 10, 10, 10, 10, 10, 2, 6, 11, 10, 2, 10, 10, 10, 10, 10, 2, 14, 3, 2, 14, 243, 10, 10, 2, 10, 10, 6, 3, 2, 6, 3, 10, 6, 11, 6]]

can_go = [[[] for i in range(60)] for j in range(60)]


pos_to_reach = {}

for i in range(len(arr_maze)):
  for j in range(len(arr_maze[i])):
    step = ['0','0','0']
    if arr_maze[i][j]&1==0:
      step = ['0','0','0']
      step[0] = i
      step[1] = j-1
      step[2] = 'h'
      can_go[i][j].append(step)

    if arr_maze[i][j] & 2 == 0:
      step = ['0', '0', '0']
      step[0] = i+1
      step[1] = j
      step[2] = 'j'
      can_go[i][j].append(step)
    
    if arr_maze[i][j]&8==0:
      step = ['0', '0', '0']
      step[0] = i-1
      step[1] = j
      step[2] = 'k'
      can_go[i][j].append(step)
    
    if arr_maze[i][j]&4==0:
      step = ['0', '0', '0']
      step[0] = i
      step[1] = j+1
      step[2] = 'l'
      can_go[i][j].append(step)
    
    if arr_maze[i][j] & 0x80 != 0:
      pos_to_reach[(arr_maze[i][j] >> 4) & 7] = [i, j, hex(arr_maze[i][j])]

print(pos_to_reach)


arr_destination = [6, 3, 7, 5, 1, 4, 0, 2]

current_pos = [0,0]
res = ''
for des in arr_destination:
  res += bfs(current_pos[0],current_pos[1],pos_to_reach[des][0],pos_to_reach[des][1],can_go) +'x'
  current_pos[0] = pos_to_reach[des][0]
  current_pos[1] = pos_to_reach[des][1]
print(res)



