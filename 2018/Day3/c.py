import re

pattern = re.compile("#(\d{1,4}) @ (\d{1,3}),(\d{1,3}): (\d{1,3})x(\d{1,3})")

# Create a set from a grid definition. Grids are defined as: "#<id> @ <x>,<y>: <w>x<h>"
def createGridSet(gridDef):
	m = pattern.match(gridDef)
	id = int(m.group(1))
	x = int(m.group(2))
	y = int(m.group(3))
	w = int(m.group(4))
	h = int(m.group(5))

	grid = set()
	startPos =  y * 1000 + x + 1
	endPos = startPos + ((h - 1) * 1000) + x + w
	rowStartPos = y * 1000 + x + 1

	for rowStartPos in range (startPos, endPos, 1000):
		for pos in range (rowStartPos, rowStartPos + w):
			grid.add(pos)

	return (id, grid)