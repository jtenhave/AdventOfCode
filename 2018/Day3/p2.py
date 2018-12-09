import re
import c

# Read grid definitions from a text file. Find the first grid that does not overlap any others.

with open("i1.txt") as input:
	lines = input.readlines()

used = set()
conflicts = set()
candidates = []

for line in lines:
	id, grid = c.createGridSet(line)
	newConflicts = grid.intersection(used)
	conflicts |= newConflicts
	used |= grid

	if not len(newConflicts) > 0:
		candidates.append((id, grid))

for id, grid in candidates:
	if len(grid.intersection(conflicts)) == 0:
		print(id)
		exit()
