from pathlib import Path
import pdb

input = Path('5/input').open().read()

seeds_str = input.split('\n\n')[0]

seeds = seeds_str.split(':')[1].split()
table_of_maps = []
for column in input.split('\n\n')[1:]:
    ranges = column.split('\n')[1:]
    table_entry = []
    for r in ranges:
        table_entry.append(r.split())
    table_of_maps.append(table_entry)

result_table = {}
for seed in seeds:
    result_table[seed] = [int(seed)]

for seed in result_table.keys():
    for column in table_of_maps:
        updated = False
        for col in column:
            d_start, s_start, length = [int(x) for x in col]
            if result_table[seed][-1] in range(s_start, s_start + length):
                offset = result_table[seed][-1] - s_start
                result_table[seed].append(d_start + offset)
                updated = True
                break
    if not updated:
        result_table[seed].append(result_table[seed][-1])

print(result_table)

locations = [result_table[x][-1] for x in result_table.keys()]
print(min(locations))