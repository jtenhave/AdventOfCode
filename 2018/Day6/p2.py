import operator
import c
import math

max_safe_distance = 10000

# A square in the grid.
class Square:

	def __init__(self, grid, safe_points, x, y):
		self.grid = grid
		self.safe_points = safe_points
		self.x = x
		self.y = y
		self.distance = None

	# Returns a list of adjacent squares.
	def getNeighbors(self):
		return [self.grid[self.y][self.x - 1], self.grid[self.y][self.x + 1], self.grid[self.y - 1][self.x], self.grid[self.y + 1][self.x]]

	# Check if neighboring squares are in the safe zone. Return the safe squares.
	def checkNeighbors(self):
		safe_neighbors = [];
		for neighbor in self.getNeighbors():
			if neighbor.checkSafe(self.distance + len(self.safe_points)):
				safe_neighbors.append(neighbor)

		return safe_neighbors

	# Check if this square is in the safe zone.
	def checkSafe(self, distance):
		if self.distance is not None:
			return False

		# Check if we are actually outside the safe zone since distance includes a buffer.
		if distance >= max_safe_distance:
			distance = self.totalDistanceFromSafe()

		self.distance = distance
		return distance < max_safe_distance

	# Calculate the total distance to all the safe points.
	def totalDistanceFromSafe(self):
		distances = map(lambda p: self.distanceToPoint(p), self.safe_points)
		return int(sum(distances))

	# Calculate the distance to a point.
	def distanceToPoint(self, point):
		return math.fabs(self.x - point[0]) + math.fabs(self.y - point[1])


# Create a grid with squares
def createGrid(xmax, xmin, ymax, ymin, safe_point):
	grid = []
	for y in range(ymin, ymax + 1):
		grid.append([])
		for x in range(xmin, xmax + 1):
			y_index = y - ymin
			grid[y_index].append(Square(grid, safe_point, x - xmin, y_index))

	return grid

# Read in a list of coordinates.
result = c.parseInput("i1.txt")

safe_points = result[0]
xmax = result [1]
xmin = result[2]
ymax = result[3]
ymin = result[4]

# Create the grid.
grid = createGrid(xmax, xmin, ymax, ymin, safe_points)

# Calculate the number of squares who sum distance to all safe points is less than 10000

# Find the starting point
start_square = grid[(ymax - ymin) >> 1][(xmax - xmin) >> 1]
start_square.distance = start_square.totalDistanceFromSafe()

current_squares = [start_square]
safe_zone_size = 1

while len(current_squares) > 0:
	next_squares = set()
	for square in current_squares:
		safe_squares = set(square.checkNeighbors())
		next_squares = next_squares | safe_squares

	safe_zone_size += len(next_squares)
	current_squares = next_squares

print(safe_zone_size)
