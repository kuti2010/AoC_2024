import numpy as np 

# Ladataan teksti tiedosto samaan muotoon matriisiksi kuin alkup. tiedostossa.
matrix = np.loadtxt("input.txt", dtype=int)

'''matrix = np.array([[3, 4],
                   [4, 3],
                   [2, 5],
                   [1, 3],
                   [3, 9],
                   [3, 3]])'''

# Määritellään lista, johon tallennetaan määrä kuinka monta kertaa luku
# ensinmäisessä sarakkeessa toistuu toisessa sarakkeessa.
counts = []

# Käydään läpi ensimmäisen sarakkeen arvot, verraten niitä vuorollaan toisen sarakkeen arvoihin
# ja tallentamalla lukumäärä uuteen vektoriin
for i in matrix[:, 0]:
    count = np.count_nonzero(matrix[:, 1] == i)
    counts.append(count)

# Muokataan 'counts' pystyvektoriksi.
counts_vector = np.array(counts).reshape(-1, 1)

# Suoritetaan ristitulo.
result = np.dot(matrix[:, 0], counts_vector)

# Tulostetaan tulos.
print(result)