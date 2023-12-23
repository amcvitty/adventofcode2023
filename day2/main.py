import sys
from lib import *

with open(sys.argv[1]) as f:
    lines = f.readlines()

total = 0
combo = [12, 13, 14]
for line in lines:
    total += game_possible(combo, line)
print(f"Part 1: {total}")

total = 0
for line in lines:
    g, rounds = parse_game(line)
    combo = max_all(rounds)
    power = combo[0] * combo[1] * combo[2]
    print(f"{g} {combo} {power}")
    total += power

print(f"Part 2: {total}")
