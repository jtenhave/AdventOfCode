import re

pattern = re.compile("([xy])=(\d*)(\.\.(\d*))?, [xy]=(\d*)(\.\.(\d*))?")

# Square in the scan. Made of either sand or clay.
class Square:
	def __init__(self, x, y):
		self.clay = False
		self.water = False
		self.wet = False
		self.x = x
		self.y = y

# A two dimensional scan of a vertical slice of ground.
class Scan:
	def __init__(self, spring):
		self.squares = []
		self.spring = spring

	# Flood the ground with water.
	def flood(self):

		# Flood using 'streams' of water. A stream ends when it either falls off the bottom of the scan
		# or when it completely fills up a container and begins to spill over the edge, creating a new stream.
		streams = [self.squares[0][self.spring]]
		finished_streams = set()

		while len(streams) > 0:

			# The start square of the stream.
			stream = streams[0]
			streams = streams[1:]

			square = stream
			while square is not None:
				square.wet = True

				# The stream has run off the bottom of the scan.
				if square.y + 1 == len(self.squares):
					square = None
				else:
					# Check if the stream has hit water or clay.
					below = self.squares[square.y + 1][square.x]
					if below.clay or below.water:
						row = [square]

						# Check if there is a either a wall or a drop off in one direction.
						def move_dir(dir):
							next = self.squares[square.y][square.x + dir]
							while True:

								# There was a wall.
								if next.clay:
									return True
								else:
									next.wet = True
									below_next = self.squares[next.y + 1][next.x]

									# There is a drop off
									if not below_next.clay and not below_next.water:
										if below_next not in finished_streams and below_next not in streams:
											streams.append(below_next)
										return False
									else:
										row.append(next)
										next = self.squares[next.y][next.x + dir]

						# Check if water can build up (i.e. there is a wall on either side)
						left_wall = move_dir(-1)
						right_wall = move_dir(1)

						# Fill the row with water.
						if left_wall and right_wall:
							for row_sqaure in row:
								row_sqaure.water = True

							# Move back up one level.
							square = self.squares[square.y - 1][square.x]
						else:
							square = None
					else:
						# Keep moving down
						square = below

			finished_streams.add(stream)

	# Convert the scan to string.
	def toString(self):
		string = ""
		for row in self.squares:
			for square in row:
				if square.y == 0 and square.x == self.spring:
					string += "+"
				elif square.clay:
					string += "#"
				elif square.water:
					string += "~"
				elif square.wet:
					string += "|"
				else:
					string += "."
			string += "\n"
		return string

# Parse a ground scan file.
def parseScanFile(file):
	with open(file) as input:
		lines = input.readlines()

	clay = []
	for line in lines:
		m = pattern.match(line.strip())

		# Parse the first range.
		x_values = [int(m.group(2))]
		if m.group(4) is not None:
			x_values = list(range(x_values[0], int(m.group(4)) + 1))

		# Parse the second range.
		y_values = [int(m.group(5))]
		if m.group(7) is not None:
			y_values = list(range(y_values[0], int(m.group(7)) + 1))

		# Swap the x and y values if needed.
		if m.group(1) == "y":
			temp_x_values = x_values
			x_values = y_values
			y_values = temp_x_values

		for y in y_values:
			for x in x_values:
				clay.append((x, y))

	# Calculate the size of the scan.
	x_max = max(clay, key=lambda c: c[0])[0]
	x_min = min(clay, key=lambda c: c[0])[0]
	y_max = max(clay, key=lambda c: c[1])[1]
	y_min = min(clay, key=lambda c: c[1])[1]

	# The width should have a buffer on either side to ensure no clay is on the edge of the scan.
	width = x_max - x_min + 3
	height = y_max - y_min + 1

	# Setup the scan.
	scan = Scan(500 - x_min + 1)
	for y in range(0, height):
		row = []
		scan.squares.append(row)
		for x in range(0, width):
			row.append(Square(x, y))

	for c in clay:
		scan.squares[c[1] - y_min][c[0] - x_min + 1].clay = True

	return scan
