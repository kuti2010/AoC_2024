# Käytettävät moduulit
import re
import numpy as np

# Eri poluille luodaan yhteinen lista
path = ['2024_05\\test.txt','2024_05\\input.txt']

# Käydään sekä testi että oikea data läpi
for x in range(0, 2):
    # Datan lukeminen
    with open(path[x], 'r') as file:
        data = file.read().splitlines()

    # Data vektoreiden ja summan alustus
    rules = []
    instr = []
    hyva_summa = 0
    hyla_summa = 0

    # Datan jakaminen
    for line in data: 
        if '|' in line:
            rules.append(line)
        elif ',' in line:
            instr.append(line)


    # Tehtävän ratkaisu loopissa, käydään yksi rivi ohjeita kerrallaan läpi
    for linex in instr:

        # Tilapäisten vektoreiden luonti
        c = []
        v = []

        # Pilkut pois ohje riviltä
        ohje = linex.split(',')

        # Keski-indeksi
        med = len(ohje) // 2

        # Tarkistetaan täyttääkö tarkistettava ohje kaikki säännöt
        for liney in rules:

            saanto = liney.split('|')
        
            if saanto[0] in ohje and saanto[1] in ohje:

                v.append(saanto)

                if ohje.index(saanto[0]) < ohje.index(saanto[1]):
                    c.append(True)
                else:
                    c.append(False)

        # Hyväksytyn ohjeen keskinmäinen alkio valitaan ja sen arvo summataan omaan muuttujaan
        if all(c):
            hyva_summa += int(ohje[med])

        # Hylätty ohje uudelleen korjataan jonka jälkeen sen keskinmäinen alkio valitaan ja sen arvo summataan omaan muuttujaan
        else:
            while not all(ohje.index(saanto[0]) < ohje.index(saanto[1])):
                for saanto in v:
                    if ohje.index(saanto[0]) > ohje.index(saanto[1]):
                        ohje[ohje.index(saanto[0])], ohje[ohje.index(saanto[1])] = ohje[ohje.index(saanto[1])], ohje[ohje.index(saanto[0])]
            hyla_summa += int(ohje[med])

    # Hyväksytyt:
    # test = 143, input = 5732
    # Hylätyt:
    # test = 123, input = 4716            

    # Tulosten tulostus
    print('\nTesti tulokset:\n') if x == 0 else print('Input tulokset:\n')
    print('Hyväksyttyjen ohje rivien keskimmäisten alkioiden summa: ' + str(hyva_summa))
    print('Korjattujen ohje rivien keskimmäisten alkioiden summa: ' + str(hyla_summa) + '\n')