import numpy as np

path = ['2024_15\\test1.txt', '2024_15\\test2.txt', '2024_15\\input.txt']

# 1406392

map = []
dire = []
directions = []

with open(path[2], 'r') as f:
    for line in f.read().splitlines():
        if '#' in line:
            map.append(list(line.strip()))
        elif ('<' or '>' or '^' or 'v') in line:
            dire.append(list(line.strip()))

dire = [i for sub in dire for i in sub]
map = np.array(map)

# [up, right, down, left] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for symb in dire:
    if symb == '^':
        directions.append((-1, 0))
    elif symb == '>':
        directions.append((0, 1))
    elif symb == 'v':
        directions.append((1, 0))
    elif symb == '<':
        directions.append((0, -1))

[x, y] = np.where(map == '@')[0][0], np.where(map == '@')[1][0]
n = 1

for i, j in directions:
    t_x, t_y = x + i, y + j
    if map[t_x,t_y] == '.':
        map[t_x,t_y] = '@'
        map[x,y] = '.'
        x, y = t_x, t_y
    elif map[t_x,t_y] == 'O':
        m = 0
        while map[t_x,t_y] == ('O'):
            t_x, t_y = t_x + i, t_y + j
            m += 1
        if map[t_x,t_y] == '.':
            map[x,y] = '.'
            x, y = x + i, y + j
            map[x,y] = '@'
            map[t_x,t_y] = 'O'
    n += 1

sum = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i,j] == 'O':
            sum += 100*i + j

print(sum)


