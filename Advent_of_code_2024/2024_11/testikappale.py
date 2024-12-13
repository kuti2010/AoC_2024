# 186203
from time import time

# Käytetyt tiedostot
path = ['2024_11\\test.txt','2024_11\\input.txt']

def blink(stones):
    result = {}
    for value, mul in stones.items():
        if not value:
            result[1] = result.get(1, 0) + mul
        elif not len(str(value)) % 2:
            val = str(value)
            val_1 = int(val[len(val) // 2:])
            val_2 = int(val[:len(val) // 2])
            result[val_1] = result.get(val_1, 0) + mul
            result[val_2] = result.get(val_2, 0) + mul
        else:
            result[value * 2024] = result.get(value * 2024, 0) + mul
    return result

if __name__ == "__main__":
    t = time()
    data = {}

    with open(path[1], 'r') as file:
        for x in file.read().split():
            data[int(x)] = 1
    loops = 75
    for _ in range(loops):
        data = blink(data)
    print(sum(data.values()))
    print(time() - t)