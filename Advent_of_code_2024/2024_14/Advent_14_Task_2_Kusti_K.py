import re
import matplotlib.pyplot as plt
import numpy as np

# 6285

def robo_move(data, x_wide, y_tall):
    n_data = {}
    for i, z in data.items():
        x = z[0] + z[2]
        y = z[1] + z[3]
        if x < 0:
            x = x_wide + x
        elif x >= x_wide:
            x = x - x_wide
        if y < 0:
            y = y_tall + y
        elif y >= y_tall:
            y = y - y_tall
        n_data[i] = [x, y, z[2], z[3]]
    return n_data

path = ['2024_14\\test.txt', '2024_14\\input.txt']
s = 7000
tar = 15

# For test
#x_wide = 11
#y_tall = 7

# For input
x_wide = 101
y_tall = 103

data = {}
i = 1

with open(path[1], 'r') as f:
    for line in f:
        num = re.findall(r'-?\d+\,-?\d+', line)
        x, y = num[0].split(',')
        u, v = num[1].split(',')
        data[i] = [int(x), int(y), int(u), int(v)]
        i += 1

lopetus = False

for i in range(1,s):
    data = robo_move(data, x_wide, y_tall)
    pic = np.full((y_tall, x_wide), ' ')
    for _, j in data.items():
        x = j[0]
        y = j[1]
        pic[y,x] = '#'
    for rivi in pic:
        for iii in range(x_wide - tar + 1):
            if all(rivi[iii+jjj] == '#' for jjj in range(tar)):
                print(i)
                lopetus = True
                break
        if lopetus:
            break
    if lopetus:
        break

x = [coor[0] for coor in data.values()]
y = [coor[1] for coor in data.values()]

plt.scatter(x, y)
plt.xlim(-1, x_wide+1)
plt.ylim(-1, y_tall+1)
plt.grid(True)
plt.gca().invert_yaxis()
plt.show()





