from pathlib import Path
import pdb

input = Path('12/input').open().read()


def validate(map, checksums):
    broken = map.split('.')
    broken_lengths = [len(x) for x in broken if x]
    return checksums == broken_lengths

def parse_unknown(map, sum_var, checksums):
    if '?' in map:
        i = map.index('?')
        parse_unknown(map[:i] + '.' + map[i + 1:], sum_var, checksums)
        parse_unknown(map[:i] + '#' + map[i + 1:], sum_var, checksums) 

    else:
        if validate(map, checksums):
            sum_var[0] += 1

sum_valids = [0]
for line in input.split('\n'):
    map, checksum_str = line.split(' ')
    checksums = [int(x) for x in checksum_str.split(',')]
    parse_unknown(map, sum_valids, checksums)

print(sum_valids[0])