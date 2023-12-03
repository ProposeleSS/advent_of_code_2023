from string import digits

with open('1/input.txt') as f:
    input = f.readlines()

def solve(input):
    result = 0
    for line in input:
        line_digits = [x for x in line if x in digits]
        str_int = ''.join([line_digits[0], line_digits[-1]])
        result = result + int(str_int)

        print(f'{line} {str_int} {result}')

    return result

print('part 1:')
print(solve(input))


digits_spelled = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)] 

input2 = []
for line in input:
    tmp_line = line
    for digit in digits_spelled:
        tmp_line = tmp_line.replace(digit[0], str(digit[1]))
    input2.append(tmp_line) 

print('part 2:')
print(solve(input2))

# kazkodel part2 atsakymo neprieme, aceit klaida
