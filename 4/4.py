from pathlib import Path
import pdb

input = Path('4/input').open().read()


points = 0
data = []

for card in input.split('\n'):
    id, numbers = card.split(':')
    winning_numbers, my_numbers = numbers.split('|')

    matching = 0
    for n in my_numbers.split():
        if n in winning_numbers.split():
            matching += 1

    data.append({
        'id': int(id.split()[1]),
        'winning_numbers': winning_numbers.split(),
        'my_numbers': my_numbers.split(), 
        'count': 1,
        'matching': matching
    })

    if matching > 0:
        points += 2**(matching -1)

print(points)

print('part 2')

total_cards = 0

for card in data:
    total_cards += card['count']
    if card['matching'] > 0:
        idx = data.index(card)
        for i in range(idx +1, idx +1 +card['matching']):
            data[i]['count'] += card['count']
            
print(total_cards)