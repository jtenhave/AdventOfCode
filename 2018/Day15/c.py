import math

elf = 0
goblin = 1

# Elf and goblin combat game.
class Game:
	def __init__(self):
		self.combatents = []
		self.board = []
		self.alive = []
		self.round = 0

	# Attack an enemy player.
	def attack(self, attacker, defender):
		defender.hp -= attacker.attack
		if defender.hp <= 0:
			defender.square.combatent = None
			self.alive.remove(defender)

	# Move to a different square.
	def move(self, combatent, square):
		combatent.square.combatent = None
		combatent.square = square
		square.combatent = combatent

	# Play the game and return the result.
	def play(self):

		for combatent in self.combatents:
			self.alive.append(combatent)

		while True:
			for combatent in self.combatents:
				if combatent not in self.alive:
					continue

				end = combatent.takeTurn();
				if end:
					return self.round * sum([combatent.hp for combatent in self.alive])

			self.combatents = [combatent for combatent in self.alive]
			self.combatents.sort(key=lambda c: (c.square.y, c.square.x))
			self.round += 1

	# Convert the game to a string value.
	def toString(self):
		string = ""
		for row in self.board:
			for square in row:
				if square.combatent != None:
					if square.combatent.team == elf:
						string += "E"
					else:
						string += "G"
				elif square.isWall:
					string += "#"
				else:
					string += "."
			string += "\n"
		return string

# A square in the game board.
class Square:
	def __init__(self, x, y, isWall, game):
		self.x = x
		self.y = y
		self.isWall = isWall
		self.game = game
		self.combatent = None
		self.neighbors = None

	# Get the neighboring squares.
	def getNeighbors(self):
		if self.neighbors is None:
			self.neighbors = []
			if self.y > 0:
				self.neighbors.append(self.game.board[self.y - 1][self.x])
			if self.x > 0:
				self.neighbors.append(self.game.board[self.y][self.x - 1])
			if self.x < len(self.game.board[0]) - 1:
				self.neighbors.append(self.game.board[self.y][self.x + 1])
			if self.y < len(self.game.board) - 1:
				self.neighbors.append(self.game.board[self.y + 1][self.x])

		return self.neighbors

# A combatent in the game.
class Combatent:
	def __init__(self, team, square, game):
		self.team = team
		self.square = square
		self.attack = 3
		self.hp = 200
		self.game = game

	# Look for a target in range to fire at.
	def getTarget(self):
		# Find the potential targets
		potential_targets = []
		for square in self.square.getNeighbors():
			if square.combatent is not None and square.combatent.team != self.team:
				potential_targets.append(square.combatent)
		
		# Find the target with the lowest hp.
		if len(potential_targets) > 0:
			min_hp_target = min(potential_targets, key=lambda t: t.hp)
			potential_targets = list(filter(lambda t: t.hp == min_hp_target.hp, potential_targets))
			return potential_targets[0]
		return None

	# Calculate the distances from a square to all other squares.
	def calculateDistances(self, to):
		distances = {}
		distance = 1
		squares = to.getNeighbors()
		while len(squares) > 0:
			next_squares = []
			for square in squares:
				if square not in distances and square.combatent is None and not square.isWall:
					distances[square] = distance
					next_squares.extend(square.getNeighbors())

			distance += 1
			squares = next_squares

		return distances

	# Find the closest square out of a set of squares to given square.
	def findClosest(self, to, squares):
		if len(squares) == 0:
			return None

		if to in squares:
			return to

		# Calculate distances.
		distances = self.calculateDistances(to)

		# Find closest squares.
		closest = []
		shortest_distance = math.inf
		for square in squares:
			if square in distances:
				distance = distances[square]
				if distance < shortest_distance:
					closest = [square]
					shortest_distance = distance
				elif distance == shortest_distance:
					closest.append(square)

		closest.sort(key=lambda s: (s.y, s.x))

		if len(closest) > 0:
			return closest[0]

		return None

	# Attempt to move in range of enemy. 
	def attemptMove(self):
		# Calculate distances.
		distances = self.calculateDistances(self.square)

		# Find remaining enemies.
		enemies = list(filter(lambda c: c.team != self.team, self.game.alive))
		if len(enemies) == 0:
			return None

		# Find squares adjacent to enemies.
		enemy_adjacent_squares = [neighbor for enemy in enemies for neighbor in enemy.square.getNeighbors()] 

		# Select a target square
		target_square = self.findClosest(self.square, enemy_adjacent_squares)

		if target_square is not None:
			# Select a path to take.
			next_square = self.findClosest(target_square, self.square.getNeighbors())
			if next_square is not None:
				self.game.move(self, next_square)
				return True
		return False

	# Performs the actions in a combatents turn.
	def takeTurn(self):
		# Check if there is an target in range
		target = self.getTarget()
		if target is None:
			# Move if there is no target.
			didMove = self.attemptMove()
			if didMove is None:
				return True

			if didMove:
				target = self.getTarget()

		# Fire at a target.
		if target is not None:
			self.game.attack(self, target)

# Parse a square in th game board.
def parseSquare(char, x, y, game, elfAttack):
	if char == '#':
		return (Square(x, y, True, game), None)

	if char == '.':
		return (Square(x, y, False, game), None)

	if char == 'G':
		square = Square(x, y, False, game)
		combatent = Combatent(goblin, square, game)
		square.combatent = combatent
		return (square,combatent)

	if char == 'E':
		square = Square(x, y, False, game)
		combatent = Combatent(elf, square, game)
		combatent.attack = elfAttack
		square.combatent = combatent
		return (square, combatent)

# Parse a game file.
def parseGameFile(file, elfAttack):

	with open(file) as input:
		lines = input.readlines()

	game = Game()
	for y, line in enumerate(lines):
		game.board.append([])
		for x, c in enumerate(line.strip()):
			(square, combatent) = parseSquare(c, x, y, game, elfAttack)
			game.board[y].append(square)
			if combatent is not None:
				game.combatents.append(combatent)

	return game
