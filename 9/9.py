from pathlib import Path
import pdb

input = Path('9/input').open().read()

def get_diff_to_zero(seq):
    result = [seq]
    while not all([x == 0 for x in result[-1]]):
        diffs = []
        for i in range(len(result[-1][1:])):
            diffs.append(result[-1][i+1] - result[-1][i])
        result.append(diffs)
    return result

def extrapolate_new_value(pyramid):
    pyramid.reverse()
    answer = 0
    previous = 0 
    for layer in pyramid[1:]:
        answer = layer[-1] + previous
        previous = answer
    return answer


extrapolated_values = []
for line in input.split('\n'):
    seq = [int(x) for x in line.split(' ')]
    pyramid = get_diff_to_zero(seq)
    extrapolated_values.append(extrapolate_new_value(pyramid))

print('part 1:')
print(sum(extrapolated_values))

extrapolated_values = []
for line in input.split('\n'):
    seq = [int(x) for x in line.split(' ')]
    seq.reverse()
    pyramid = get_diff_to_zero(seq)
    extrapolated_values.append(extrapolate_new_value(pyramid))

print(sum(extrapolated_values))