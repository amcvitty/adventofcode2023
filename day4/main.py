import sys
from lib import *

with open(sys.argv[1]) as f:
    lines = f.readlines()


def get_matches(line):
    _, x = line.split(":")
    wins, have = x.split("|")
    wins = [int(x) for x in wins.split()]
    have = [int(x) for x in have.split()]

    matches = []
    for h in have:
        if h in wins:
            matches.append(h)
    return matches


total = 0
for line in lines:
    matches = get_matches(line)
    points = pow(2, len(matches) - 1) if matches else 0
    total += points
print(f"Part1: { total}")


total = 0
cards = []
for c, line in enumerate(lines):
    copies = cards.pop(0) + 1 if len(cards) > 0 else 1
    print(f"Card {c+1}: {copies}")
    matches = get_matches(line)
    for m in range(0, len(matches)):
        if m >= len(cards):
            cards.append(copies)
        else:
            cards[m] += copies
    # points = pow(2, len(matches) - 1) * copies if matches else 0
    # print(line, matches, points)
    total += copies
print(f"Part2: { total}")
