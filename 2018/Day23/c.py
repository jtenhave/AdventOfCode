import re 
import math

pattern = re.compile("pos=<([\d-]*),([\d-]*),([\d-]*)>, r=(\d*)")

class Coord:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.neighbors = None
		self.distance_origin = None

	def distance(self, coord):
		return math.fabs(coord.x - self.x) + math.fabs(coord.y - self.y) + math.fabs(coord.z - self.z)

	def getDistanceFromOrigin(self):
		if self.distance_origin is None:
			self.distance_origin = self.distance(Coord(0,0,0))

		return self.distance_origin

	def getNeighbors(self):
		if neighbors is None:
			self.neighbors = []
			self.neighbors.append(c.Coord(self.x - 1, self.y, self.z))
			self.neighbors.append(c.Coord(self.x + 1, self.y, self.z))
			self.neighbors.append(c.Coord(self.x, self.y - 1, self.z))
			self.neighbors.append(c.Coord(self.x, self.y + 1, self.z))
			self.neighbors.append(c.Coord(self.x, self.y, self.z - 1))
			self.neighbors.append(c.Coord(self.x, self.y, self.z + 1))

		return neighbors

	def toString(self):
		return str(self.x) + "," + str(self.y) + "," + str(self.z)

class Nanobot:
	def __init__(self, coord, r):
		self.coord = coord
		self.r = r
		self.x_max = Coord(coord.x + r, coord.y, coord.z)
		self.x_min = Coord(coord.x - r, coord.y, coord.z)
		self.y_max = Coord(coord.x, coord.y + r, coord.z)
		self.y_min = Coord(coord.x, coord.y - r, coord.z)
		self.z_max = Coord(coord.x, coord.y, coord.z + r)
		self.z_min = Coord(coord.x, coord.y, coord.z - r)
		self.corners = [self.x_max, self.x_min, self.y_max, self.y_min, self.z_max, self.z_min]

	def distance(self, nanobot):
		return self.coord.distance(nanobot.coord)

	def contains(self, coord):
		return self.coord.distance(coord) <= self.r

	def toString(self):
		return self.coord.toString() + ":" + str(self.r)

def parseNanobotFile(file):

	with open(file) as input:
		lines = input.readlines()

	nanobots = []
	for line in lines:
		m = pattern.match(line.strip())

		x = int(m.group(1))
		y = int(m.group(2))
		z = int(m.group(3))
		r = int(m.group(4))

		nanobots.append(Nanobot(Coord(x, y, z), r))

	return nanobots
