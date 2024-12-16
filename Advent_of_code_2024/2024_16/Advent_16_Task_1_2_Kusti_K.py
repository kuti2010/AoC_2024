import heapq
from math import inf

def maze(data):
    maze = ''
    for row in data:
        for i in row:
            maze += ' ' + i
        print(maze)
        maze = ''

def node(data, node):
    m = len(data)
    n = len(data[0])
    for i in range(m):
        for j in range(n):
            if data[i][j] == node:
                return (i, j)
            
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
    pq = []
    
    # Start node: (cost, node, dir, path)
    heapq.heappush(pq, (0, start_node, (0, 1), []))

    visited = dict()
    best_paths = []
    best_reachables = set()
    highscore = inf
    directions_map = {(-1, 0): 'UP', (0, 1): 'RIGHT', (1, 0): 'DOWN', (0, -1): 'LEFT'}

    while pq:
        total_cost, current_node, last_direction, path = heapq.heappop(pq)

        if total_cost > highscore:
            break

        if (current_node, last_direction) in visited and visited[(current_node, last_direction)] < total_cost:
            continue

        visited[(current_node, last_direction)] = total_cost
        neighbours = maze_graph[current_node]

        if current_node == end_node:
            highscore = total_cost
            best_paths.append(path + [current_node])        

        for node in neighbours:
            row, col = node
            direction = None
            if row == current_node[0] - 1:  # UP
                direction = (-1, 0)
            elif row == current_node[0] + 1:  # DOWN
                direction = (1, 0)
            elif col == current_node[1] + 1:  # RIGHT
                direction = (0, 1)
            elif col == current_node[1] - 1:  # LEFT
                direction = (0, -1)

            additional_cost = 0
            if last_direction is not None:
                if direction != last_direction:
                    last_dir_str = directions_map[last_direction]
                    new_dir_str = directions_map[direction]
                    
                    if (last_dir_str == 'UP' and new_dir_str in ['LEFT', 'RIGHT']) or \
                       (last_dir_str == 'DOWN' and new_dir_str in ['LEFT', 'RIGHT']) or \
                       (last_dir_str == 'LEFT' and new_dir_str in ['UP', 'DOWN']) or \
                       (last_dir_str == 'RIGHT' and new_dir_str in ['UP', 'DOWN']):
                        additional_cost = 1000

            new_cost = total_cost + additional_cost + 1

            if node not in visited:
                new_path = path + [current_node]
                heapq.heappush(pq, (new_cost, node, direction, new_path))

    if best_paths:
        for path in best_paths:
            for node in path:
                best_reachables.add(node)

        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if maze[row][col] != '#':
                    if (row, col) in best_reachables:
                        maze[row][col] = 'O'
    return maze, highscore


path = ['2024_16\\test1.txt', '2024_16\\test2.txt', '2024_16\\input.txt']
data = []
sum = 0

with open(path[2], 'r') as f:
    for line in f.read().splitlines():
        data.append(list(line.strip()))

S_node = node(data, 'S')
E_node = node(data, 'E')
maze_graph = trans_g(data)
solved_maze, hihgscore = solve_maze(data, maze_graph, S_node, E_node)

for i in range(len(solved_maze)):
    for j in range(len(solved_maze[0])):
        if solved_maze[i][j] == 'O':
            sum += 1

print('Shortest path: ' + str(hihgscore))
print('All seats: ' + str(sum))
#maze(solved_maze)