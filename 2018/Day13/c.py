
direction = { "UP": 0, "RIGHT": 1, "DOWN": 2, "LEFT": 3 }
turn = { "LEFT": -1, "STRAIGHT": 0, "RIGHT": 1 }

# Get the next track segment that the cart will occupy.
def getNextTrackSegment(tracks, cart):
	if cart.dir == direction["UP"]:
		return tracks[cart.seg.y - 1][cart.seg.x]

	if cart.dir == direction["RIGHT"]:
		return tracks[cart.seg.y][cart.seg.x + 1]

	if cart.dir == direction["DOWN"]:
		return tracks[cart.seg.y + 1][cart.seg.x]
		
	if cart.dir == direction["LEFT"]:
		return tracks[cart.seg.y][cart.seg.x -1]

# A cart.
class Cart:
	def __init__(self, dir, seg):
		self.dir = dir
		self.next_turn = turn["LEFT"]
		self.seg = seg

	# Turn the cart.
	def turn(self, turn):
		#print("old dir " + str(self.dir))
		self.dir = self.dir + turn
		#print("new dir " + str(self.dir))
		if self.dir < 0:
			self.dir = direction["LEFT"]

		if self.dir > 3:
			self.dir = direction["UP"]

	# Decide the new driection when at an intersection.
	def chooseNextDirection(self):
		self.turn(self.next_turn)

		self.next_turn += 1
		if self.next_turn > 1:
			self.next_turn = turn["LEFT"]

	# Change the direction when going around a corner.
	def forceChangeDirection(self, track):
		if track == '/':
			if self.dir == direction["UP"] or self.dir == direction["DOWN"]:
				self.turn(turn["RIGHT"])
			else:
				self.turn(turn["LEFT"])
		else:
			if self.dir == direction["UP"] or self.dir == direction["DOWN"]:
				self.turn(turn["LEFT"])
			else:
				self.turn(turn["RIGHT"])

	# Change the carts direction if needed.
	def changeDirection(self, seg):
		if seg.type == '+':
			self.chooseNextDirection()
		elif seg.type == '/' or seg.type == '\\':
			self.forceChangeDirection(seg.type)

	# Move the cart to its new track segment.
	def moveTo(self, new_seg):
		self.seg.cart = None
		new_seg.cart = self

		self.seg = new_seg
		self.changeDirection(self.seg)

# A segment of track.
class Track:
	def __init__(self, type, x, y):
		self.type = type
		self.cart = None
		self.x = x
		self.y = y

# Parse a segment of track. Return the track, and a cart if necessary.
def parseTrackSegment(seg, x, y):
	if seg == ' ':
		return (None, None)

	if seg == '^':
		track = Track('|', x, y)
		return (track,  Cart(direction["UP"], track))

	if seg == '>':
		track = Track('-', x, y)
		return (track,  Cart(direction["RIGHT"], track))

	if seg == 'v':
		track = Track('|', x, y)
		return (track,  Cart(direction["DOWN"], track))

	if seg == '<':
		track = Track('-', x, y)
		return (track,  Cart(direction["LEFT"], track))

	return (Track(seg, x, y), None)

# Parse a will with tracks and carts.
def parseTrackFile(file):
	tracks = []
	carts = []

	with open(file) as input:
		lines = input.readlines()

	for y, line in enumerate(lines):
		track_row = []
		tracks.append(track_row)

		for x, seg in enumerate(line):
			(track, cart) = parseTrackSegment(seg, x, y)
			track_row.append(track)
		
			if cart is not None:
				track.cart = cart
				carts.append(cart)

	return (tracks, carts)
