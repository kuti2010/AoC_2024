# Ladataa Moduulit
import numpy as np

# Loopin testaus aliohjelma
def loop_test(data,directions,dire,x,y,block_history):
    tdata = np.copy(data) # Kopioidaan data
    tdire = dire
    tx = x
    ty = y
    counter = 0
    [x_max, y_max] = tdata.shape # max ja min
    coor_history = set() # Luodaan uniikki lista käydyistä ruudukoista
    # Esteen lisäys dataan
    nx, ny = directions[tdire]
    tdata[x + nx, y + ny] = '#'

    # Lopetaan jos lisätty este on jo aikaisemmin polun varrella, muuten lisätään uusi este listaan
    if ((x+nx,y+ny)) in block_history:
            return counter
    block_history.add((x+nx,y+ny))

    # Testataan polku jos looppi syntyy tai ei
    while 0 < tx < x_max - 1 and 0 < ty < y_max - 1:

        # Jos ruutu on tullut jo polulla vastaan niin lopetettan, koska looppi on syntynyt
        if (tx,ty,tdire) in coor_history:
            counter = 1
            break
        
        # Lisätään uusi käyty ruutu listaan
        coor_history.add((tx,ty,tdire))
        nx, ny = directions[tdire]
        xx = tx + nx
        yy = ty + ny

        # Käännytään myötäpäivään, jos este on edessä. Muuten liikutaan eteenpäin.
        if tdata[xx, yy] == '#':
            tdire = (tdire + 1) % 4
        else:
            tx = xx
            ty = yy    
    return counter

# Käytetyt polut
path = ['2024_06\\test.txt','2024_06\\input.txt']

# Testin ja input ratkaisu for loopissa
for i in range(0, 2):
    data = []
    block_history = set()
    loop_counter = 0

    with open(path[i], 'r') as f:
        for line in f:
            data.append(list(line.strip()))

    data = np.array(data)

    # Lisätään vartijan lähtöpaikka esteeksi
    [x, y] = np.where(data == '^')[0][0], np.where(data == '^')[1][0]
    block_history.add((x,y))

    [x_max, y_max] = data.shape
    # [up, right, down, left] = [0, 1, 2, 3]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dire = 0
    # Suoritetaan vartijan reitti sokkelossa
    while 0 < x < x_max - 1 and 0 < y < y_max - 1:
        
        loop_counter += loop_test(data,directions,dire,x,y,block_history)

        data[x, y] = 'X'
        nx, ny = directions[dire]
        if data[x + nx, y + ny] in ['.', 'X']:
            x += nx
            y += ny
        elif data[x + nx, y + ny] == '#':
            dire = (dire + 1) % 4

    # Tulokset:
    # Testi:
    # The final area covered by the guard in grids is 41.
    # There are 6 loop opportunities in the area.

    # Input:
    # The final area covered by the guard in grids is 4776.
    # There are 1586 loop opportunities in the area.

    data[x,y] = 'X'
    print('\nTesti:') if i == 0 else print('\nInput:')
    print('The final area covered by the guard in grids is ' + str(np.count_nonzero(data == 'X')) + '.')
    print('There are ' + str(loop_counter) + ' loop opportunities in the area.')