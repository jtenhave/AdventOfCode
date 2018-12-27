# A room in the facility.
class Room:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.above = None
		self.right = None
		self.below = None
		self.left = None
		self.distance = None

# A path though the facility.
class Path:
	def __init__(self, facility, start):
		self.room = start
		self.facility = facility
	
	# Move in a certain direction.
	def move(self, dir):
		if dir == 'N':
			room = self.facility.getRoom(self.room.x, self.room.y + 1)
			self.room.above = room
			room.below = self.room

			self.room = room

		elif dir == 'E':
			room = self.facility.getRoom(self.room.x + 1, self.room.y)
			self.room.right = room
			room.left = self.room

			self.room = room
		elif dir == 'S':
			room = self.facility.getRoom(self.room.x, self.room.y - 1)
			self.room.below = room
			room.above = self.room

			self.room = room
		elif dir == 'W':
			room = self.facility.getRoom(self.room.x -1, self.room.y)
			self.room.left = room
			room.right = self.room

			self.room = room

# Facility full of rooms.
class Facility:
	def __init__(self):
		self.room_map = {}
		self.rooms = []
		self.xmax = 0
		self.ymax = 0
		self.xmin = 0
		self.ymin = 0

	# Get a room in the facility.
	def getRoom(self, x, y):
		if not y in self.room_map:
			self.room_map[y] = {}

		if not x in self.room_map[y]:
			room = Room(x, y)
			self.room_map[y][x] = room
			self.rooms.append(room)

		if x > self.xmax:
			self.xmax = x

		if y > self.ymax:
			self.ymax = y

		if x < self.xmin:
			self.xmin = x

		if y < self.ymin:
			self.ymin = y

		return self.room_map[y][x]

# Parse a file with paths through a facility.
def parseFacilityFile(file):

	with open("i1.txt") as input:
		lines = input.readlines()

	facility = Facility()
	start = facility.getRoom(0, 0)
	path = Path(facility, start)
	paths = [path]

	# Parse the paths.
	for line in lines:
		for c in line.strip():
			if c == '(':
				new_path = Path(facility, path.room)
				paths.append(path)
				path = new_path

			elif c == ')':
				path = paths.pop(-1)

			elif c == '|':
				parent = paths[-1]
				new_path = Path(facility, parent.room)
				path = new_path
			
			elif c != '^' and c != '$':
				path.move(c)

	# Compute the distance to each room.
	round = [start]
	distance = 0
	while len(round) > 0:
		next_round = []
		distance += 1
		for room in round:
			above = room.above
			if above is not None and above.distance is None:
				above.distance = distance
				next_round.append(above)

			right = room.right
			if right is not None and right.distance is None:
				right.distance = distance
				next_round.append(right)

			below = room.below
			if below is not None and below.distance is None:
				below.distance = distance
				next_round.append(below)

			left = room.left
			if left is not None and left.distance is None:
				left.distance = distance
				next_round.append(left)

		round = next_round

	return facility