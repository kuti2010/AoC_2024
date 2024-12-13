# Task 1 ratkaisu: 6519155389266
example = ['12345','2333133121414131402','2333133121414131402123456789','1010101010101010101010']
raw_data = '2024_09\\input.txt'

with open(raw_data,'r') as f:
        d = f.read().splitlines()

data = example + d
data = list(map(int, data[4]))

flip = 1
data2 = []
id = 0

for i in data:
    if flip == 1:
        flip = 0
        data2.extend([id] * i)
        id += 1
    elif flip == 0:
        flip = 1
        data2.extend(['.'] * i)

i = 0
while i < len(data2):
    if data2[i] == '.':
        for ind in range(len(data2)-1, -1, -1):
            if str(data2[ind]).isdigit():
                data2[i], data2[ind] = data2[ind], data2[i]
                i += 1
                break
        if all(x == '.' for x in data2[i+1:]):
            break
    else:
        i += 1

tulos = 0

for i, merkki in enumerate(data2):
    if merkki != '.':
        tulos += int(merkki) * i



print(tulos)