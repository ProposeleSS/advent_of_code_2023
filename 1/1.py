from string import digits
import re
import pdb

with open('1/input.txt') as f:
    input = f.readlines()

def solve(input):
    result = 0
    for line in input:
        line_digits = [x for x in line if x in digits]
        str_int = ''.join([line_digits[0], line_digits[-1]])
        result = result + int(str_int)

    return result

print('part 1:')
print(solve(input))


digits_spelled = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9} 

input2 = []
for line in input:
    tmp_line = line
    idxs = {}
    for digit in digits_spelled.keys():
        # idx = tmp_line.find(digit)
        idx = [m.start() for m in re.finditer(digit, line)]
        if len(idx) > 0:
            idxs[digit] = idx
    idxs_sorted = sorted(idxs.items(), key=lambda x: x[1])
    if len(idxs_sorted) > 0:
        first = idxs_sorted[0]
        last = idxs_sorted[-1]
        # if len(first[1]) > 1:
        #     first[1] = [first[1][0]]
        # if len(last[1]) > 1:
        #     last[1] = [last[1][-1]]
        tmp_line = tmp_line.replace(first[0], str(digits_spelled[first[0]]))
        tmp_line = str(digits_spelled[last[0]]).join(tmp_line.rsplit(last[0], 1))

    input2.append(tmp_line) 


print('part 2:')
print(solve(input2))

# kazkodel part2 atsakymo neprieme, aceit klaida
 