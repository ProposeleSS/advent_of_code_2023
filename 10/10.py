from pathlib import Path
import pdb

input = Path('10/test2').open().read()
matrix = [list(line) for line in input.split('\n')]

max_y = len(matrix) -1
max_x = len(matrix[0]) -1

possible_dirs_start = {
    'n': ['|', 'F', '7'],
    'e': ['-', 'J', '7'],
    's': ['|', 'L', 'J'],
    'w': ['-', 'F', 'L']
}

possible_dirs = {
    '|': ['n', 's'],
    '-': ['e', 'w'],
    'L': ['n', 'e'],
    'J': ['n', 'w'], 
    '7': ['w', 's'], 
    'F': ['e', 's']
}

opposite_dirs = {
    'n': 's',
    'e': 'w',
    's': 'n',
    'w': 'e'
}

move_map = {
    'n': (-1, 0),
    'e': (0, +1),
    's': (+1, 0),
    'w': (0, -1),
}

# find S:
for y in range(max_y):
    for x in range(max_x):
        if matrix[y][x] == 'S':
            s = [y, x]
            break
print(s)

def get_nesw(xy):
    try:
        return {
            'n': None if xy[0] == 0 else matrix[xy[0]-1][xy[1]],
            'e': None if xy[1] == max_x else matrix[xy[0]][xy[1]+1],
            's': None if xy[0] == max_y else matrix[xy[0]+1][xy[1]],
            'w': None if xy[1] == 0 else matrix[xy[0]][xy[1]-1],
        }
    except IndexError:
        pdb.set_trace()

def get_possible_dirs_start(xy):
    neighbours = get_nesw(xy)
    results = []
    for key, val in neighbours.items():
        if val in possible_dirs_start[key]:
            results.append(key)
    return results

# get length of the loop:
current_position = s
# start first possible direction:
current_direction = get_possible_dirs_start(s)[0]
previous_direction = None
log = [(s, 'S')]
steps = 0

while 'S' not in get_nesw(current_position)[current_direction]:
    # move towards direction:
    current_position[0] += move_map[current_direction][0]
    current_position[1] += move_map[current_direction][1]

    dirs = possible_dirs[matrix[current_position[0]][current_position[1]]]
    for dir in dirs:
        if dir != opposite_dirs[current_direction]:
            current_direction = dir
            break
    
    log.append((current_position.copy(), current_direction))
    steps += 1

print('part 1')
print(steps // 2 + 1)

# clean up map from unused pipes:
matrix_clean = []
for y in range(max_y + 1):
    matrix_clean.append(['.' for _ in range(max_x + 1)])


for entry in log:
    y, x = entry[0]
    matrix_clean[y][x] = matrix[y][x]


area = 0
for row in matrix_clean:
    idx_y = matrix_clean.index(row)
    loop_edges = [x[0] for x in log if matrix_clean[x[0][0]][x[0][1]] in 'SJLF7|' and x[0][0] == matrix_clean.index(row)]
    loop_edges.sort(key=lambda x: x[1])
    dots = []
    for i in range(max_x):
        if row[i] == '.':
            dots.append((idx_y, i))
            pass
    pdb.set_trace()

print('part 2')
print(area)        