import itertools

# Tehtävän yksi vastaukset: Testi = 11387 ja Input = 509463489296712'''

# Käytetyt polut
path = ['2024_07\\test.txt', '2024_07\\input.txt']

# Lasketaan tulos kummallekin tiedostolle
for p in range(1):
    with open(path[p], 'r') as file:
        data = file.read().splitlines()

    summa = 0

    # Käydään tiedostossa olevat rivit läpi
    for line in data:
        vastaukset_str, numerot_str = line.split(':')
        vastaukset = int(vastaukset_str)
        numerot = list(map(int, numerot_str.strip().split()))

        merkit = ['+', '*', '||']
        
        # Alustetaan laskutoimitus
        yhdistelmat = itertools.product(merkit, repeat=len(numerot) - 1)

        # Käydään kaikki mahdolliset laskutoimitus-yhdistelmät
        for yhdistelmä in yhdistelmat:
            tulos = numerot[0]
            for i, merkki in enumerate(yhdistelmä):
                if merkki == '+':
                    tulos += numerot[i + 1]
                elif merkki == '*':
                    tulos *= numerot[i + 1]
                elif merkki == '||':
                    tulos = int(str(tulos) + str(numerot[i + 1]))

            if vastaukset == tulos:
                summa += tulos
                break

    print(summa)
