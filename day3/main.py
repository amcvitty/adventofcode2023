import sys
from lib import *

with open(sys.argv[1]) as f:
    lines = f.readlines()

width = len(lines[0])
height = len(lines)

# We expand the grid one e=in each direction to make the search easier!
blank_row = "".join(["." for _ in range(0, width + 1)])

grid = [blank_row] + [("." + line.strip() + ".") for line in lines] + [blank_row]

numbers = []
for i, row in enumerate(grid):
    row_numbers = [(number, i, j1, j2) for (number, j1, j2) in find_numbers(row)]
    print(row + " " + ",".join([str(n) for n in row_numbers]))
    numbers += row_numbers

#### Find the part_numbers
part_numbers = []
for number, i, j1, j2 in numbers:
    coords = find_surrounding_coords(i, j1, j2)
    if any([is_symbol(grid, i, j) for (i, j) in coords]):
        print(number)
        part_numbers.append(number)

print("Part 1: " + str(sum(part_numbers)))

#### Find the gears
gears = []

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == "*":
            gears.append((i, j))
part2 = 0
for gi, gj in gears:
    matches = []
    for number, i, j1, j2 in numbers:
        coords = find_surrounding_coords(i, j1, j2)
        if any([gi == i and gj == j for (i, j) in coords]):
            matches.append(number)
    if len(matches) == 2:
        print(matches[0], matches[1], matches[0] * matches[1])
        part2 += matches[0] * matches[1]
print("Part 2: " + str(part2))
