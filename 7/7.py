from pathlib import Path
import pdb

input = Path('7/test').open().read()

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
match_ranks = [([5], 7),
               ([4], 6),
               ([3, 2], 5),
               ([2, 3], 5),
               ([3], 4),
               ([2, 2], 3),
               ([2], 2),
               ([], 1)
               ]

hands = []
for entry in input.split('\n'):
    hand, bid = entry.split()
    matches = []
    for card in cards:
        matching = len([x for x in hand if x == card])
        if matching > 1: 
            matches.append(matching)
        matches_ranked = [x[1] for x in match_ranks if x[0] == matches][0]
    hands.append((hand, matches_ranked, bid))

print(hands)

# for hand in hands:
#     for idx in range(len(hands) - 1):
#         if hands[idx]['matching']