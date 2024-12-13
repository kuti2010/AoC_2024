# Task 2
# Testi = 34, Input = 1417

import numpy as np
from collections import defaultdict

path = ['2024_08\\test.txt', '2024_08\\input.txt']

data = []
symbols = set()
node = set()
fre = 0

with open(path[1], 'r') as f:
    for line in f:
        data.append(list(line.strip()))
        symbols.update(line.strip())

symbols.remove('.')
symbols = list(symbols)
symbol_dict = defaultdict(list)

data = np.array(data)
x_m, y_m = data.shape

# Etsitään kaikki symbolien sijainnit ja tallennetaan coordinaatit oman elementinsä listoille
symbol_positions = {symbol: np.argwhere(data == symbol) for symbol in symbols}

for symbol, coor in symbol_positions.items():
    for i in range(len(coor)):
        for j in range(len(coor)):
            if i != j:
                dx = -(coor[i][0] - coor[j][0])
                dy = -(coor[i][1] - coor[j][1])
                nx = coor[i][0] + dx
                ny = coor[i][1] + dy
                while 0 <= nx < x_m and 0 <= ny < y_m:
                    if data[nx][ny] == '.':
                        data[nx][ny] = '#'
                        fre += 1
                    elif data[nx][ny] not in ('.','#'):
                        node.add((nx,ny))
                    nx += dx
                    ny += dy

fre += len(node)

print(data)
print(fre)