from pathlib import Path
import pdb

input = Path('12/test').open().read()


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

print('part 1')
print(sum_valids[0])

#  need more optimal algorithm, this just takes too long
# for line in input.split('\n'):
#     map, checksum_str = line.split(' ')
#     checksums = [int(x) for x in checksum_str.split(',')]
#     map_unfolded = '?'.join([map, map, map, map, map])
#     checksums_unfolded = []
#     for _ in range(5):
#         checksums_unfolded.extend(checksums)
#     parse_unknown(map_unfolded, sum_valids, checksums_unfolded)

# print('part 2')
# print(sum_valids[0])
