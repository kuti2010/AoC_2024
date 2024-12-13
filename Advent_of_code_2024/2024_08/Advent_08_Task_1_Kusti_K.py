# Task 1
# Testi = 14, Input = 413


import re
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

[x_m, y_m] = data.shape

for symbol in symbols:
    for i in range(x_m):
        for j in range(y_m):
            if data[i][j] == symbol:
                symbol_dict[symbol].append((i,j))



for symbol, group in symbol_dict.items():
    for i in range(len(group)):
        for j in range(len(group)):
            if i != j:
                x_d = -2*(group[i][0] - group[j][0])
                y_d = -2*(group[i][1] - group[j][1])
                nx = group[i][0] + x_d
                ny = group[i][1] + y_d
                if (0 <= nx < x_m and 0 <= ny < y_m):
                    if data[nx][ny] == '.':
                        data[nx][ny] = '#'
                        fre += 1
                    elif data[nx][ny] != ('.' and '#'):
                        node.add((nx,ny))

fre += len(node)


print(data)
print(fre)