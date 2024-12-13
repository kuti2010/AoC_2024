# Task 2 ratkaisu: 6547228115826
# Paras aika: 99s
# data[1] = 2858

import time

start_time = time.time()

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

ls_p = -1
while abs(ls_p) < len(data2):
    last_number = None

    if data2[ls_p] == '.':
         ls_p -= 1
    else:
        for ind in range(len(data2) + ls_p, -1, -1):
            if last_number is None:
                if str(data2[ind]).isdigit():
                    last_number = str(data2[ind])
                    last_number_ind = ind
                    count = 1
            elif str(data2[ind]) == last_number:
                count += 1
            else:
                break
        for ind in range(len(data2) + ls_p-1):
            if data2[ind:ind+count] == ['.'] * (count):
                data2[ind:ind+count], data2[last_number_ind-count+1:last_number_ind+1] = data2[last_number_ind-count+1:last_number_ind+1], data2[ind:ind+count]
                break
        ls_p -= count


tulos = sum(int(merkki) * i for i, merkki in enumerate(data2) if merkki != '.')

print(tulos)

end_time = time.time()
execution_time = end_time - start_time
print(f"Koodin suoritus kesti {execution_time} sekuntia.")