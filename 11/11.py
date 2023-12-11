from pathlib import Path
import pdb

input = Path('11/input').open().read()

matrix = [list(line) for line in input.split('\n')]

def get_empty_idx(matrix):
    empty = []
    for i in range(len(matrix)):
        if all([x=='.' for x in matrix[i]]):
            empty.append(i)
            continue
    return empty

empty_rows = get_empty_idx(matrix)
empty_columns = get_empty_idx(list(zip(*matrix)))

galaxies = []

for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] == '#':
            galaxies.append((y, x))

path_sum = 0
for i in range(len(galaxies[:-1])):
    for j in range(i+1, len(galaxies)):
        path = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        y_limits = [galaxies[i][0], galaxies[j][0]]
        x_limits = [galaxies[i][1], galaxies[j][1]]
        y_extra = len([y for y in empty_rows if y in range(min(y_limits), max(y_limits))])
        x_extra = len([x for x in empty_columns if x in range(min(x_limits), max(x_limits))])
        path_sum += path + y_extra + x_extra

print('part 1')
print(path_sum)

path_sum_2 = 0
for i in range(len(galaxies[:-1])):
    for j in range(i+1, len(galaxies)):
        path = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        y_limits = [galaxies[i][0], galaxies[j][0]]
        x_limits = [galaxies[i][1], galaxies[j][1]]
        y_extra = len([y for y in empty_rows if y in range(min(y_limits), max(y_limits))])
        x_extra = len([x for x in empty_columns if x in range(min(x_limits), max(x_limits))])
        path_sum_2 += path + (y_extra * 999999) + (x_extra * 999999)

print('part 2')
print(path_sum_2)