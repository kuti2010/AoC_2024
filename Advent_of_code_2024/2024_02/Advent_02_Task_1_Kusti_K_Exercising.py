import numpy as np

file_path = 'input.txt'  # Replace with the actual path to the file

safe_count = 0
with open(file_path, 'r') as file: # with avaa tiedoston väliaikaisesti käyttöön
    for line in file: # käydään rivi kerrallaan läpi
        # Parse each line into a list of integers
        report = list(map(int, line.split()))# split() muuttaa datan string listaksi, map() muokkaa string valuttuun muotoon tässä
        # tässä tapauksessa int eli kokonaisluvuiksi ja list() muokkaa kokonaisluvut listaksi
        levels = np.array(report) # poistaa riviltä välimerkit ja ottaa vain vektorin
        diffs = np.diff(levels)
        np.all(np.abs(diffs) >= 1) #and np.all(np.abs(diffs) <= 3)
        



        #   safe_count += 1
# return safe_count