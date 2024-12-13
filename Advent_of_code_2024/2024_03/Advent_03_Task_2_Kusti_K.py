import numpy as nu
import re

summa = 0 # Alustetaan loppusumma

with open('2024_03\\input.txt', 'r') as file:
    data = ''.join(line.strip() for line in file) # yhdistetään 6 riviä stringiä yhdeksi pötköksi
    
    
    cut_data = re.sub(r'don\'t\(\).*?(do\(\)|$)', '', data) # Poistetaan stringistä kohdat jotka
# alkavat "don't() ja päättyvät joko do() tai rivin loppuun"


    mul_data = re.findall(r'mul\(\d+,\d+\)',cut_data) # Valitaan vain mul(1,2) kohdat

    for pairs in mul_data:
        clean_data = re.findall(r'\d+,\d+', pairs) # Valitaan vain mul() sisällä olevat alkiot
        for multip in clean_data:
            part = multip.split(',') # Muutetaan , => välilyönniksi
            tulo = int(part[0]) * int(part[1]) # Kerto lasku
        summa += nu.sum(tulo) # Summaus
print(summa) # Lopputulos