import re
import numpy as nu

input_path = '2024_04\\input.txt'

test_path = '2024_04\\test.txt'

word_count = 0

with open(input_path, 'r') as file:
    data = file.read().splitlines()

for row in range(1,len(data)-1):
    for col in range(1,len(data)-1):
        if data[row][col] == 'A':

            if data[row-1][col-1] == 'M' and data[row-1][col+1] == 'M' and data[row+1][col-1] == 'S' and data[row+1][col+1] == 'S':
                word_count += 1
            
            elif data[row-1][col-1] == 'S' and data[row-1][col+1] == 'M' and data[row+1][col-1] == 'S' and data[row+1][col+1] == 'M':
                word_count += 1

            elif data[row-1][col-1] == 'S' and data[row-1][col+1] == 'S' and data[row+1][col-1] == 'M' and data[row+1][col+1] == 'M':
                word_count += 1

            elif data[row-1][col-1] == 'M' and data[row-1][col+1] == 'S' and data[row+1][col-1] == 'M' and data[row+1][col+1] == 'S':
                word_count += 1

print(word_count)
