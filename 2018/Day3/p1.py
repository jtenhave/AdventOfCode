import re
import c

# Read grid definitions from a text file. Count the number of the cells that are overlapped by multiple grids.

with open("i1.txt") as input:
	lines = input.readlines()

used = set()
conflicts = set()

for line in lines:
	_, grid = c.createGridSet(line)
	conflicts |= grid.intersection(used) 
	used |= grid

print(len(conflicts))
