
tree = '|'
lumber_yard = '#'
bare = '.'

# A lumber collection area.
class Area():
	def __init__(self):
		self.patches = []

	# Advance area to the next minute.
	def advanceMinute(self):
		for row in self.patches:
			for patch in row:
				patch.computeNextType()

		for row in self.patches:
			for patch in row:
				patch.applyNextType()

	# Compute the result of the current lumber area.
	def computeResult(self):
		lumber_yards = 0
		trees = 0
		for row in self.patches:
			for patch in row:
				if patch.type == lumber_yard:
					lumber_yards += 1
				elif patch.type == tree:
					trees += 1
		return lumber_yards  * trees
	
	# Create a string representation of the current lumber area.
	def toString(self):
		string = ""
		for row in self.patches:
			for patch in row:
				string += patch.type

			string += "\n"
		return string

# A patch in the lumber collection area.
class Patch():
	def __init__(self, area, type, x, y):
		self.area = area
		self.type = type
		self.x = x
		self.y = y
		self.neighbors = None
		self.next_type = None

	# Get the neighboring patches.
	def getNeighbors(self):
		if self.neighbors is None:
			self.neighbors = []
			at_top = self.y == 0
			at_left = self.x == 0
			at_bottom = self.y + 1 == len(self.area.patches)
			at_right = self.x + 1 == len(self.area.patches[0])

			if not at_top:
				self.neighbors.append(self.area.patches[self.y - 1][self.x])
				if not at_left:
					self.neighbors.append(self.area.patches[self.y - 1][self.x - 1])
				if not at_right:
					self.neighbors.append(self.area.patches[self.y - 1][self.x + 1])

			if not at_bottom:
				self.neighbors.append(self.area.patches[self.y + 1][self.x])
				if not at_left:
					self.neighbors.append(self.area.patches[self.y + 1][self.x - 1])
				if not at_right:
					self.neighbors.append(self.area.patches[self.y + 1][self.x + 1])

			if not at_left:
				self.neighbors.append(self.area.patches[self.y][self.x - 1])

			if not at_right:
				self.neighbors.append(self.area.patches[self.y][self.x + 1])

		return self.neighbors

	# Compute the next type for the patch.
	def computeNextType(self):
		if self.type == bare:
			adjacent_trees = 0
			for patch in self.getNeighbors():
				if patch.type == tree:
					adjacent_trees += 1

				if adjacent_trees == 3:
					self.next_type = tree
					return

		elif self.type == tree:
			adjacent_lumber_yards = 0
			for patch in self.getNeighbors():
				if patch.type == lumber_yard:
					adjacent_lumber_yards += 1

				if adjacent_lumber_yards == 3:
					self.next_type = lumber_yard
					return

		else:
			adjacent_lumber_yards = 0
			adjacent_trees = 0
			for patch in self.getNeighbors():
				if patch.type == lumber_yard:
					adjacent_lumber_yards += 1
				elif patch.type == tree:
					adjacent_trees += 1

				if adjacent_trees > 0 and adjacent_lumber_yards > 0:
					return
			self.next_type = bare

	# Apply the next type to patch.
	def applyNextType(self):
		if self.next_type is not None:
			self.type = self.next_type
			self.next_type = None

# Parse a lumber collection area.
def parseCollectionArea(file):
	with open(file) as input:
		lines = input.readlines()

	area = Area()
	for y, line in enumerate(lines):
		row = []
		area.patches.append(row)
		for x, c in enumerate(line.strip()):
			row.append(Patch(area, c, x, y))

	return area
