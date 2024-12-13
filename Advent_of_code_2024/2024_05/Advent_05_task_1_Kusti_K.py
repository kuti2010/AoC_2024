import re
import numpy as np

test_path = '2024_05\\test.txt'

input_path = '2024_05\\input.txt'

with open(input_path, 'r') as file:
    data = file.read().splitlines()

rules = []
instr = []

summa = 0

for line in data:
    if re.match(r'^\d+(\|\d+)+$', line):
        rules.append(line)
    elif re.match(r'^\d+(,\d+)+$', line):
        instr.append(line)

for linex in instr:

    c = []

    ohje = linex.split(',') # eka 75,47,61,53,29

    med = int(int(len(ohje)) / 2 - 0.5) # Keski-indeksi

    for liney in rules:

        saanto = liney.split('|')
        if saanto[0] in ohje and saanto[1] in ohje: # eka 75|47

            if ohje.index(saanto[0]) < ohje.index(saanto[1]):
                c.append(True)
            else:
                c.append(False)
        
    if all(c):
        summa += int(ohje[med])

print(summa)
    
            