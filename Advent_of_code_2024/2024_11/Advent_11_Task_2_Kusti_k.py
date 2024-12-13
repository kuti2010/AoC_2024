# 221291560078593
from time import time
t_1 = time()

def ali(data):
    result = {}
    for luku, m in data.items():
        if not luku:
            result[1] = result.get(1, 0) + m
        elif not len(str(luku)) % 2:
            val = str(luku)
            val_1 = int(val[len(val) // 2:])
            val_2 = int(val[:len(val) // 2])
            result[val_1] = result.get(val_1, 0) + m
            result[val_2] = result.get(val_2, 0) + m
        else:
            result[luku * 2024] = result.get(luku * 2024, 0) + m
    return result

# Käytetyt tiedostot
path = ['2024_11\\test.txt','2024_11\\input.txt']
data = {}

with open(path[0], 'r') as f:
    for i in f.read().split():
        data[int(i)] = 1


all_blinks = 6
for _ in range(all_blinks):
    print(data)
    data = ali(data)
    
all_rock = sum(data.values())

print(all_rock)
print(time() - t_1)