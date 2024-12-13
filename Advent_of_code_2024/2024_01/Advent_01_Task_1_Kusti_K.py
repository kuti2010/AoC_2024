import numpy as np 

# Ladataan teksti tiedosto samaan muotoon matriisiksi kuin alkup. tiedostossa.
input = np.loadtxt("input.txt", dtype=int)
# Järjestetään sarakkeet pienimmästä suurinpaan.
sorted_input = np.sort(input, axis=0)
# Lasketaan jokaisen rivillä olevien numeroiden etäisyys.
distances = np.abs(np.diff(sorted_input, axis=1))
# Lasketaan loppu summa.
total_distance = np.sum(distances)

# Lopputulos.
print(total_distance)