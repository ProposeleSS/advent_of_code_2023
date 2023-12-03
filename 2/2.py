from pathlib import Path
import pdb

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

input = Path('2/input').open().read()

valid_games = set()
data = []
for line in input.split('\n'):
    split_line = line.split(':')
    game_id = int(split_line[0].split()[1])
    games = split_line[1].split(';')
    fail = None
    red = 0
    green = 0
    blue = 0

    for game in games:
        for entry in game.split(','):
            count, color = entry.split()
            if color == 'red': 
                if red < int(count):
                    red = int(count)
                if int(count) > MAX_RED:
                    print(f'{game_id}: found max red: {game}')
                    fail = True

            if color == 'green':
                if green < int(count):
                    green = int(count)
                if int(count) > MAX_GREEN:
                    print(f'{game_id}: found max green: {game}')
                    fail = True

            if color == 'blue':
                if blue < int(count):
                    blue = int(count)
                if int(count) > MAX_BLUE:
                    print(f'{game_id}: found max blue: {game}')
                    fail = True

    if not fail:
        valid_games.add(game_id)
    data.append({
        'id': game_id,
        'red': red,
        'green': green,
        'blue': blue
    })
print(sum(valid_games))

print('part2')

powers = []
for game in data:
    game['power'] = game['red'] * game['green'] * game['blue']
    print(game)
    powers.append(game['power'])

print(sum(powers))