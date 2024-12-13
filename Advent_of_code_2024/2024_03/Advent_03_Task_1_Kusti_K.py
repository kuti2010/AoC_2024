
import numpy as nu
import re

summa = 0 # Määritetään loppu summa

with open('2024_03\\input.txt', 'r') as file:
    for lines in file:
        kerto = [] # Määritetään väliaikais kertolasku vektori
        
        result = re.findall(r'mul\(\d+,\d+\)',lines) # Poimitaan mul(1,2) tyyppiset alkiot


        for line in result:
            result2 = re.findall(r'\d+,\d+',line) # Poimitaan mul() sisältä numerot
            for lin in result2:
                part = lin.split(',') # pilkku => välilyönniksi
                tulo = int(part[0]) * int(part[1]) # Kertolasku
            
            kerto.append(tulo) # Vektoriin lisäys
        summa += nu.sum(kerto) # Summaus
print(summa) # vastaus