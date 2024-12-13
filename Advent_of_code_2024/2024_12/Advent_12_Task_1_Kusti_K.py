import numpy as np
import re
from collections import defaultdict

def dfs(data, i, j, ch_sym, symbol_dict, sym):

    if data[i][j] != ch_sym:
        return
    
    if (i,j) in symbol_dict[sym]:
        return
    symbol_dict[sym].append((i,j))

    # Moving up, right, down, and left one by one
    n = len(data)
    m = len(data[0])
    if i - 1 >= 0: # up
        dfs(data, i - 1, j, ch_sym, symbol_dict, sym)
    if j + 1 < m: # right
        dfs(data, i, j + 1, ch_sym, symbol_dict, sym)
    if i + 1 < n: # down
        dfs(data, i + 1, j, ch_sym, symbol_dict, sym)
    if j - 1 >= 0: # left
        dfs(data, i, j - 1, ch_sym, symbol_dict, sym)

path = ['2024_12\\test1.txt', '2024_12\\test2.txt', '2024_12\\test3.txt', '2024_12\\input.txt']
data = []
uni = set()

with open(path[3], 'r') as f:
    for line in f:
        data.append(list(line.strip()))
        uni.update(line.strip())

symbols = list(sorted(uni))
symbol_dict = defaultdict(list)
data = np.array(data)
print(data)

[x_m, y_m] = data.shape
sym = 0

for i in range(x_m):
    for j in range(y_m):
        if not any((i, j) in value for value in symbol_dict.values()):
            ch_sym = data[i][j]
            dfs(data, i, j, ch_sym , symbol_dict, sym)
            sym += 1

sum = 0

for symbol, group in symbol_dict.items():
    per = 0
    area = len(group)
    for sym in group:
        if (sym[0], sym[1] - 1) not in group:
            per += 1
        if (sym[0] + 1, sym[1]) not in group:
            per += 1
        if (sym[0], sym[1] + 1) not in group:
            per += 1
        if (sym[0] - 1, sym[1]) not in group:
            per += 1
    sum += area * per

print(sum)