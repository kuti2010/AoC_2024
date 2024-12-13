import numpy as np
import re
from collections import defaultdict

# Task 2, 858684

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

symbol_dict = defaultdict(list)
data = np.array(data)
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
    area = len(group)
    per = 0
    for i in range(x_m):
        con_up = 0
        con_down = 0
        for j in range(y_m):
            if (i, j) in group:
                if (i - 1, j) not in group and con_up == 0: # up
                    per += 1
                    con_up = 1
                if (i + 1, j) not in group and con_down == 0: # down
                    per += 1
                    con_down = 1
                if (i - 1, j) in group and con_up == 1: # up
                    con_up = 0
                if (i + 1, j) in group and con_down == 1: # down
                    con_down = 0
            else:
                con_up = 0
                con_down = 0

    for j in range(y_m):
        con_right = 0
        con_left = 0
        for i in range(x_m):
            if (i, j) in group:
                if (i, j + 1) not in group and con_right == 0: # right
                    per += 1
                    con_right = 1
                if (i, j - 1) not in group and con_left == 0: # left
                    per += 1
                    con_left = 1
                if (i, j + 1) in group and con_right == 1: # right
                    con_right = 0
                if (i, j - 1) in group and con_left == 1: # left
                    con_left = 0
            else:
                con_right = 0
                con_left = 0
    sum += area * per
print(sum)
