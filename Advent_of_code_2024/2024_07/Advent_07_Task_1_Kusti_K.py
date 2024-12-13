import numpy as np
import re
import itertools
# Käytetyt polut
path = ['2024_07\\test.txt','2024_07\\input.txt']

for p in range(2):
    with open(path[p], 'r') as file:
        data = file.read().splitlines()

    vastaukset = []
    numerot = []
    summa = 0

    for line in data:
        osa = line.split(':')
        vastaukset.append(osa[0])
        numerot.append(osa[1].strip())

    merkit = ['+', '*']

    for laskutoimitus in range(len(vastaukset)):
        yhdistelmat = itertools.product(merkit, repeat=(len(numerot[laskutoimitus].split())-1))
        for yhdistelmä in yhdistelmat:
            # Alustetaan laskutoimitus
            tulos = int(numerot[laskutoimitus].split()[0])
            # Käydään merkki_lista läpi ja tehdään laskutoimitukset
            for i, merkki in enumerate(yhdistelmä):
                if merkki == '+':
                    tulos += int(numerot[laskutoimitus].split()[i + 1])
                elif merkki == '*':
                    tulos *= int(numerot[laskutoimitus].split()[i + 1])
            if int(vastaukset[laskutoimitus]) == tulos:
                summa += tulos
                break

    print(summa)


# Tehtävän yksi vastaukset: Testi = 3749 ja Input = 3312271365652
        
