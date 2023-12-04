from pathlib import Path
from string import digits
import pdb

input = Path('4/input').open().read()


points = 0

for card in input.split('\n'):
    numbers = card.split(':')[1]
    winning_numbers, my_numbers = numbers.split('|')

    matching = 0
    for n in my_numbers.split():
        if n in winning_numbers.split():
            matching += 1

    if matching > 0:
        points += 2**(matching -1)

print(points)