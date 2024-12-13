import numpy as np
import time

start_time = time.time()


# Task 1 , 667

# Käytetyt tiedostot
path = ['2024_10\\test.txt','2024_10\\input.txt']

data = []

with open(path[1], 'r') as f:
    for line in f:
        data.append(list(map(int, line.strip())))


# [up, right, down, left] = [0, 1, 2, 3]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

data = np.array(data)

hike = 0
print(data)

def polut(i,j,hike):
    for x,y in directions:
        x_n, y_n = i + x, j + y
        if 0 <= x_n < len(data) and 0 <= y_n < len(data[0]) and data[x_n][y_n] - data[i][j] == 1:
            if data[x_n][y_n] == 9:
                hike += 1
            else:
                hike = polut(x_n,y_n,hike)
    return hike

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 0:
            hike = polut(i,j,hike)

print(hike)

end_time = time.time()
execution_time = end_time - start_time
print(f"Koodin suoritus kesti {execution_time} sekuntia.")