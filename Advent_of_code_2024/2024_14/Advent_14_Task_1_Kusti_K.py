import re

# 215476074

path = ['2024_14\\test.txt', '2024_14\\input.txt']

s = 100

# For test
#x_wide = 11
#y_tall = 7
# For input
x_wide = 101
y_tall = 103

x_n = x_wide // 2
y_n = y_tall // 2

q_1 = 0
q_2 = 0
q_3 = 0
q_4 = 0

with open(path[1], 'r') as f:
    for line in f:
        num = re.findall(r'-?\d+\,-?\d+', line)
        x, y = num[0].split(',')
        u, v = num[1].split(',')
        x = int(x)
        y = int(y)
        u = int(u)
        v = int(v)
        for i in range(s):
            x += u
            y += v
            if x < 0:
                x = x_wide + x
            elif x >= x_wide:
                x = x - x_wide
            if y < 0:
                y = y_tall + y
            elif y >= y_tall:
                y = y - y_tall
        if not (x == x_n or y == y_n):
            if (x_n < x < x_wide and 0 <= y < y_n): # Q 1
                q_1 += 1
            elif (0 <= x < x_n and 0 <= y < y_n): # Q 2
                q_2 += 1
            elif (0 <= x < x_n and y_n < y < y_tall): # Q 3
                q_3 += 1
            elif (x_n < x < x_wide and y_n < y < y_tall): # Q 4
                q_4 += 1
    sol = q_1 * q_2 * q_3 * q_4
    print(sol)
