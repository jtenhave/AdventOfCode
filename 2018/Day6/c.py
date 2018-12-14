import math
import re

pattern = re.compile("(\d{1,3}), (\d{1,3})")

# Parse an input file of coordinates
def parseInput(file):
	with open(file) as input:
		lines = input.readlines()

	points = []
	xmax = -math.inf
	xmin = math.inf
	ymax = -math.inf
	ymin = math.inf
	for line in lines:
		m = pattern.match(line)
		point = (int(m.group(1)), int(m.group(2)))

		# Track min and max value.
		if point[0] > xmax:
			xmax = point[0]
		if point[0] < xmin:
			xmin = point[0]
		if point[1] > ymax:
			ymax = point[1]
		if point[1] < ymin:
			ymin = point[1]

		points.append(point)

	return (points, xmax, xmin, ymax, ymin)