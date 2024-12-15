import numpy as np

path = ['2024_15\\test3.txt', '2024_15\\test2.txt', '2024_15\\input.txt']

# 1429013

def findBox(x, y):
    if map[x, y] == "[": return [x, y+1]
    else: return [x, y-1]

map = []
dire = []
directions = []

with open(path[2], 'r') as f:
    for line in f.read().splitlines():
        if '#' in line:
            map.append(list(line.strip()))
        elif ('<' or '>' or '^' or 'v') in line:
            dire.append(list(line.strip()))

map = np.array(map)
dire = [i for sub in dire for i in sub]

n_map = np.full((len(map),len(map[0])*2), '#')
for i in range(1, len(map)-1):
    for j in range(1, len(map[0])-1):
        if map[i,j] == '.':
            n_map[i,j*2] = '.'
            n_map[i,j*2+1] = '.'
        elif map[i,j] == 'O':
            n_map[i,j*2] = '['
            n_map[i,j*2+1] = ']'
        elif map[i,j] == '@':
            n_map[i,j*2] = '@'
            n_map[i,j*2+1] = '.'
map = n_map
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
    elif (map[t_x, t_y] in ('[', ']')) and ((i, j) == (0, 1) or (i, j) == (0, -1)):
        while map[t_x,t_y] in ('[', ']'):
            t_x, t_y = t_x + i, t_y + j
        if map[t_x,t_y] == '.':
            t_x, t_y = t_x - i, t_y - j
            while map[t_x,t_y] in ('[', ']'):
                map[t_x + i,t_y + j] = map[t_x,t_y]
                t_x, t_y = t_x - i, t_y - j
            map[x,y] = '.'
            x, y = x + i, y + j
            map[x,y] = '@'
    elif (map[t_x, t_y] in ('[', ']')) and ((i, j) == (-1, 0) or (i, j) == (1, 0)):
        # Had to look for help to get this part done right
        con = [[t_x, t_y], findBox(t_x, t_y)]
        for a, b in con:
            if map[a+i, b] == "[" or map[a+i, b] == "]":
                con.extend([[a+i, b], findBox(a+i, b)])
        if any(map[a+i, b] == "#" for a, b in con):
            continue
        con = list(set((int(a), int(b)) for a, b in con))
        if i < 0:
            con.sort()
        else:
            con.sort(reverse=True)
        for a, b in con:
            map[a + i, b] = map[a, b]
            map[a, b] = "."
        map[t_x,t_y] = '@'
        map[x,y] = '.'
        x, y = t_x, t_y
    n += 1

sum = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i,j] == '[':
            sum += 100*i + j

print(sum)


