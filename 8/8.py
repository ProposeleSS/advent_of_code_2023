from pathlib import Path
import pdb
from math import  lcm

input = Path('8/input').open().read()

pattern_str, *node_str = input.split('\n\n')

pattern = [0 if x == 'L' else 1 for x in pattern_str]

nodes = {}
for node in node_str[0].split('\n'):
    key, values = node.split(' = ')
    val1, val2 = values.replace('(', '').replace(')','').split(', ')
    nodes[key] = (val1, val2)

key = 'AAA'
steps = 0
while(key != 'ZZZ'):
    idx = pattern[steps % len(pattern)]
    key = nodes[key][idx] 
    steps += 1


print('part 1:')
print(steps)

print('part 2:')

keys = [x for x in nodes.keys() if x.endswith('A')]
results = []

for key in keys:
    steps = 0
    while(not key.endswith('Z')):
        idx = pattern[steps % len(pattern)]
        key = nodes[key][idx] 
        steps += 1
    results.append(steps)


print(lcm(*results))