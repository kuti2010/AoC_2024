# 186203
import numpy as np
import time

start_time = time.time()

# Käytetyt tiedostot
path = ['2024_11\\test.txt','2024_11\\input.txt']

# Lue tiedosto ja jaa se numpy-taulukoksi
with open(path[1], 'r') as f:
    data = np.array(f.read().split(), dtype=object)

# Asetetaan kaikki blinks
all_blinks = 25

# Optimoidaan data käsittely numpy:n avulla
for ite in range(all_blinks):
    ind = 0
    while ind < len(data):
        if data[ind] == '0':
            data[ind] = '1'
            ind += 1
        elif len(data[ind]) % 2 == 0:
            le = len(data[ind]) // 2
            new_value = str(int(data[ind][le:]))  # Arvon laskeminen kerran
            # Luodaan uusi taulukko
            data = np.insert(data, ind + 1, new_value)
            data[ind] = data[ind][:le]  # Päivitetään alkuperäinen arvo
            ind += 2
        else:
            data[ind] = str(int(data[ind]) * 2024)
            ind += 1

# Lasketaan "all_rock" - arvo
all_rock = len(data)

# Tulostetaan tulos
print(all_rock)

end_time = time.time()
execution_time = end_time - start_time
print(f"Koodin suoritus kesti {execution_time} sekuntia.")