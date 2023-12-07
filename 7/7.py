from pathlib import Path
import pdb

input = Path('7/input').open().read()

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


n = len(hands)
for i in range(n-1):
    for j in range(0, n-i-1):
        if hands[j][1] > hands[j + 1][1]:
            hands[j], hands[j + 1] = hands[j + 1], hands[j]
        elif hands[j][1] == hands[j + 1][1]:
            for k in range(len(hands[j][0])):
                if cards.index(hands[j][0][k]) < cards.index(hands[j+1][0][k]):
                    hands[j], hands[j + 1] = hands[j + 1], hands[j]
                    break
                elif cards.index(hands[j][0][k]) > cards.index(hands[j+1][0][k]):
                    break

print(sum([int(x[2]) * (hands.index(x) + 1) for x in hands]))