import operator
import math
import re

pattern = re.compile("(\d{1,3}), (\d{1,3})")

# A city made of blocks. Divded into neighborhoods.
class City:
	def __init__(self):
		self.blocks = []
		self.neighborhood_sizes = {}

# A city block.
class Block:

	def __init__(self, city, x, y):
		self.city = city
		self.claims = []
		self.x = x
		self.y = y
		self.neighborhood = None
		self.made = False

	# Returns a list of adjacent blocks.
	def getNeighbors(self):
		return [self.city.blocks[self.y][self.x - 1], self.city.blocks[self.y][self.x + 1], self.city.blocks[self.y - 1][self.x], self.city.blocks[self.y + 1][self.x]]

	# Attempt to claim neighboring blocks for this block's neighborhood
	def claimNeighbors(self):
		self.claimed_neighbors = []
		self.made = True
		for neighbor in self.getNeighbors():
			if neighbor.claim(self.neighborhood):
				self.claimed_neighbors.append(neighbor)

	# Check the status of the claims made on neightboring blocks.
	def checkNeighborClaims(self):
		claimed = []
		for neighbor in self.claimed_neighbors:
			if neighbor.checkClaim() == self.neighborhood:
				claimed.append(neighbor)
		self.made = False
		return claimed

	# Attempt to claim this block for a given neighborhood.
	def claim(self, neighborhood):
		if self.neighborhood is None:
			self.claims.append(neighborhood)
			return True
		return False

	# Check the claims made on this block. Return the neighborhood id of a successful claim.
	def checkClaim(self):
		if self.neighborhood is None:
			claims = set(self.claims)
			neighborhood = -1
			if len(claims) == 1:
				neighborhood = next(iter(claims))
				if neighborhood in self.city.neighborhood_sizes:
					self.city.neighborhood_sizes[neighborhood] += 1
			
			self.neighborhood = neighborhood
			return neighborhood

		return -1

# A city block on the edge of town
class EdgeBlock(Block):
	def __init__(self, city, x, y):
		Block.__init__(self, city, x, y)

	def getNeighbors(self):
		neighbors = []
		if self.x > 0:
			neighbors.append(self.city.blocks[self.y][self.x - 1])
		if self.x < len(self.city.blocks[0]) - 1:
			neighbors.append(self.city.blocks[self.y][self.x + 1])
		if self.y > 0:
			neighbors.append(self.city.blocks[self.y - 1][self.x])
		if self.y < len(self.city.blocks) - 1:
			neighbors.append(self.city.blocks[self.y + 1][self.x])
		return neighbors;

	def checkClaim(self):
		neighborhood = super().checkClaim()
		if neighborhood >= 0 and neighborhood in self.city.neighborhood_sizes:
			del self.city.neighborhood_sizes[neighborhood]
		return neighborhood


# Parse an input file with city neighborhood centers
def parseInput(file):
	with open(file) as input:
		lines = input.readlines()

	neighborhood_centers = []
	xmax = -math.inf
	xmin = math.inf
	ymax = -math.inf
	ymin = math.inf
	for line in lines:
		m = pattern.match(line)
		center = (int(m.group(1)), int(m.group(2)))

		# Track min and max value.
		if center[0] > xmax:
			xmax = center[0]
		if center[0] < xmin:
			xmin = center[0]
		if center[1] > ymax:
			ymax = center[1]
		if center[1] < ymin:
			ymin = center[1]

		neighborhood_centers.append(center)

	return (neighborhood_centers, xmax, xmin, ymax, ymin)

# Create a city with blocks
def createCity(xmax, xmin, ymax, ymin):
	
	city = City()

	# Initialize the top row of blocks
	city.blocks.append([])
	for x in range(xmin, xmax + 1):
		city.blocks[0].append(EdgeBlock(city, x - xmin, 0))

	# Initialize the inner blocks
	for y in range(ymin + 1, ymax):
		city.blocks.append([])
		y_index = y - ymin
		city.blocks[y_index].append(EdgeBlock(city, 0, y_index))

		for x in range(xmin + 1, xmax):
			city.blocks[y_index].append(Block(city, x - xmin, y_index))

		city.blocks[y_index].append(EdgeBlock(city, xmax - xmin, y_index))

	# Initialize the bottom row of blocks
	city.blocks.append([])
	y_index = ymax - ymin;
	for x in range(xmin, xmax + 1):
		city.blocks[y_index].append(EdgeBlock(city, x - xmin, y_index))

	return city

def createCityWithNeighborhoods(file):

	# Read in a list of characters. Remove all pairs that are the same letter with opposite capitalization.
	result = parseInput("i1.txt")

	neighborhood_centers = result[0]
	xmax = result [1]
	xmin = result[2]
	ymax = result[3]
	ymin = result[4]

	city = createCity(xmax, xmin, ymax, ymin)

	current_blocks = []

	# Setup the inital round of block claims
	for i, center in enumerate(neighborhood_centers):
		block = city.blocks[center[1] - ymin][center[0] - xmin]
		city.neighborhood_sizes[i] = 0
		block.claim(i)
		block.checkClaim()
		current_blocks.append(block)

	while len(current_blocks) > 0:
		next_blocks = []
		for block in current_blocks:
			block.claimNeighbors()

		for block in current_blocks:
			claimed = block.checkNeighborClaims()
			next_blocks.extend(claimed)

		current_blocks = next_blocks

	return city

# Read in a list of neighborhood centers. Each block is part of the neighborhood whos center it is closest to.
# Find the largest neighborhood, excluding neighborhoods touching the edge of town (assumed to be infinite in size)

city = createCityWithNeighborhoods("i1.txt")

largest_neighborhood = max(city.neighborhood_sizes.items(), key=operator.itemgetter(1))
print(largest_neighborhood)
