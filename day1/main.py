import sys
from lib import *

with open(sys.argv[1]) as f:
    lines = f.readlines()

count = 0
for line in lines:
    ints = get_ints(line)
    f = ints[0]
    l = ints[-1]
    count += 10 * f + l

print(count)
