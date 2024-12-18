from queue import Queue
import numpy as np

def trans_g(data):
    graph = {}
    maze_size = len(data)
    row_size = len(data[0])

    for row in range(maze_size):
        for col in range(row_size):
            if data[row][col] != '#':
                adj_nodes = []

                if row+1 < maze_size and data[row+1][col] != '#': # DOWN
                    adj_nodes.append((row+1, col))
                if row-1 >= 0 and data[row-1][col] != '#': # UP
                    adj_nodes.append((row-1, col))
                if col+1 < row_size and data[row][col+1] != '#': # RIGHT
                    adj_nodes.append((row, col+1))
                if col-1 >= 0 and data[row][col-1] != '#': # LEFT
                    adj_nodes.append((row, col-1))
                graph[(row, col)] = adj_nodes

    return graph

def solve_maze(maze, maze_graph, start_node, end_node):
    visited = []
    start_path = [start_node]
    q = Queue()
    q.put(start_path)

    while not q.empty():
        path = q.get()
        neighbours = maze_graph[path[-1]]

        for node in neighbours:
            if node == end_node:
                for coordinate in path:
                    row, col = coordinate
                    maze[row][col] = 'O'
                return maze
            
            if node not in visited:
                visited.append(node)
                new_path = path + [node]
                q.put(new_path)
    return maze

path = ['2024_18\\test.txt', '2024_18\\input.txt']
data = []
q = 0

with open(path[q], 'r') as f:
    for line in f.read().splitlines():
        data.append(list(map(int, line.split(','))))

x,y = (7, 7) if q == 0 else (71, 71)
b = len(data)
S = (0,0)
E = (x-1,y-1)

while True:  
    gr = np.full((x,y),'.')
    ii = 0
    for i in data:
        gr[i[1]][i[0]] = '#'
        ii += 1
        if ii == b:
            break
    maze_graph = trans_g(gr)

    solved_maze = solve_maze(gr, maze_graph, S, E)
    if np.any(solved_maze == 'O'):
        print(",".join(map(str, data[b])))
        break
    else:
        b -= 1