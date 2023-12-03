from pathlib import Path
from string import digits
import pdb

input = Path('3/input').open().read()
input_matrix = [list(x) for x in input.split('\n')]

max_y = max_x = len(input_matrix)

def get_numbers(input_matrix):
    numbers = []
    for line in input_matrix:
        symbol = 0
        while symbol < len(line):
            if line[symbol] in digits:
                # get whole int not only first digit:
                idx = symbol
                idx_end = idx
                while line[idx_end] in digits and idx_end +1 < max_x:
                    idx_end += 1

                print(line[idx:])
                number = int(''.join(line[idx:idx_end]))
                y_idx = input_matrix.index(line)
                numbers.append({
                    'value': number,
                    'y': y_idx,
                    'x_start': idx,
                    'x_end': idx_end -1
                })
                symbol = idx_end
            symbol += 1

    return numbers

def check_if_part_no(input_matrix, numbers):
    part_numbers = []
    for number in numbers:
        search_index_list = set()
        # top row above number:
        if number['y'] > 0:
            for idx in range(number['x_start'], number['x_end']+1):
                search_index_list.add((number['y'] - 1, idx))

        # botom row below number:
        if number['y'] + 1 < max_y:
            for idx in range(number['x_start'], number['x_end']+1):
                search_index_list.add((number['y'] + 1, idx))

        # left column:
        if number['x_start'] > 0:
            search_index_list.add((number['y'], number['x_start'] -1))
            if number['y'] > 0:
                search_index_list.add((number['y'] - 1, number['x_start'] -1))
            if number['y'] +1 < max_y:
                search_index_list.add((number['y'] + 1, number['x_start'] -1))

        # right column:
        if number['x_end'] +1 < max_x:
            search_index_list.add((number['y'], number['x_end'] +1))
            if number['y'] > 0:
                search_index_list.add((number['y'] - 1, number['x_end'] +1))
            if number['y'] +1 < max_y:
                search_index_list.add((number['y'] + 1, number['x_end'] +1))

        for idx in search_index_list:
            char = input_matrix[idx[0]][idx[1]]
            if char != '.' and char not in digits:
                part_numbers.append(number['value'])
                number['is_part_no'] = True
                number['symbol_xy'] = idx
                continue

    return part_numbers

numbers = get_numbers(input_matrix)
part_numbers = check_if_part_no(input_matrix, numbers)
for n in numbers:
    if n.get('is_part_no', False):
        print(n)
print(sum(part_numbers))