import re
import numpy as nu

input_path = '2024_04\\input.txt'

test_path = '2024_04\\test.txt'

word_count = 0


with open(input_path, 'r') as file:
    data = file.read().splitlines()

# Tarkistetaan horisontaalisesti
for line in data:
    word_count += line.count('XMAS') + line.count('SAMX')


# Tarkistetaan vertikaalisesti
list_data = [list(lin) for lin in data]

tr_list_data = nu.array(list_data).T

for tr_line in tr_list_data:
    tr_data = ''.join(tr_line)
    word_count += tr_data.count('XMAS') + tr_data.count('SAMX')

# Tarkistetaan diagonaalit
diagonaalit = []

# Päädiagonaali
diagonaalit.append([data[i][i] for i in range(len(data))])

# Alatason diagonaalit
for d in range(1, len(data)):
    diagonaalit.append([data[i+d][i] for i in range(len(data)-d)])

# Ylätason diagonaalit
for d in range(1, len(data)):
    diagonaalit.append([data[i][i+d] for i in range(len(data)-d)])

# Vastadiagonaali
diagonaalit.append([data[i][len(data)-1-i] for i in range(len(data))])

# Alatason vastadiagonaalit
for d in range(1, len(data)):
    diagonaalit.append([data[i+d][len(data)-1-i] for i in range(len(data)-d)])

# Ylätason vastadiagonaalit
for d in range(1, len(data)):
    diagonaalit.append([data[i][len(data)-1-i-d] for i in range(len(data)-d)])

for diag in diagonaalit:
    diag_data = ''.join(diag)
    word_count += diag_data.count('XMAS') + diag_data.count('SAMX')

print(word_count)