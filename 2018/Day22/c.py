import math

rocky = '.'
wet = '='
narrow = '|'
types = [rocky, wet, narrow]

neither = 0
torch = 1
climbing_gear = 2

# A region in the cave.
class Region:
	def __init__(self, cave, x, y, geologic_index, depth):
		self.cave = cave
		self.x = x
		self.y = y
		self.geologic_index = geologic_index
		self.erosion_level = (geologic_index + depth) % 20183
		self.risk_level = self.erosion_level % 3
		self.type = types[self.risk_level]
		self.neighbors = None
		self.distances = { neither: math.inf, torch: math.inf, climbing_gear: math.inf  }

	# Get the region's tools.
	def getTools(self):
		if self.type == rocky:
			return { torch, climbing_gear}
		if self.type == wet:
			return { neither, climbing_gear}
		if self.type == narrow:
			return { neither, torch }

	# Check if it is possible to move though the region with a given tool.
	def canMoveThrough(self, tool):
		if tool is None:
			return False

		return tool in self.getTools()

	# Ge the neighboring regions.
	def getNeighbors(self):
		if self.neighbors is None:
			self.neighbors = []
			if self.y > 0:
				self.neighbors.append(self.cave.regions[self.y - 1][self.x])
			if self.x > 0:
				self.neighbors.append(self.cave.regions[self.y][self.x - 1])
			if self.x < len(self.cave.regions[0]) - 1:
				self.neighbors.append(self.cave.regions[self.y][self.x + 1])
			if self.y < len(self.cave.regions) - 1:
				self.neighbors.append(self.cave.regions[self.y + 1][self.x])

		return self.neighbors

# A cave made of different regions.
class Cave:
	def __init__(self):
		self.regions = []

# Create a cave object for the given parameters
def createCave(target_x, target_y, depth, buffer_x, buffer_y):
	risk_level = 0;
	cave = Cave()
	for y in range(0, target_y + 1 + buffer_y):
		row = []
		cave.regions.append(row)
		for x in range(0, target_x + 1 + buffer_x):
			geologic_index = 0
			if y == 0:
				if x > 0:
					geologic_index = x * 16807
			elif x == 0:
				if y > 0:
					geologic_index = y * 48271
			elif x != target_x or y != target_y:
				geologic_index = cave.regions[y - 1][x].erosion_level * cave.regions[y][x - 1].erosion_level

			region = Region(cave, x, y, geologic_index, depth)
			row.append(region)

			risk_level += region.risk_level

	return (cave, risk_level)
