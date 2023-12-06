from pathlib import Path
import pdb

input = Path('6/input').open().read()

times, distances = input.split('\n')

data = zip(times.split()[1:], distances.split()[1:])

results = 1
for time, threshold in data:
    count = 0
    for delay in range(int(time)):
        result = delay * (int(time) - delay)
        if result > int(threshold):
            count += 1
    results *= count

print("part 1:")
print(results)

time = int(''.join(times.split()[1:]))
threshold = int(''.join(distances.split()[1:]))

count = 0
for delay in range(time):
    result = delay * (time - delay)
    if result > threshold:
        count += 1

print('part 2:')
print(count)