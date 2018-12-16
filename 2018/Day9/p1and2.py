# The special divisor which determines if a marble is worth points.
special = 23

# A player in the marble game.
class Player:
	def __init__(self):
		self.points = 0

# A marble in the game.
class Marble:
	def __init__(self, value):
		self.value = value

# The marbles in play.
class Marbles:
	def __init__(self, init_value):
		marble = Marble(init_value)
		marble.next = marble
		marble.prev = marble

		self.current = marble
	
	# Push a marble into the marble ring.
	def pushMarble(self, value):
		marble = Marble(value)

		# Always add marbles one clockwise of the current marble.
		before = self.current.next
		after = self.current.next.next

		after.prev = marble
		marble.next = after

		before.next = marble
		marble.prev = before

		self.current = marble

	# Remove a marble from the marble ring.
	def popMarble(self):
		marble = self.current

		# Always remove marbles seven counter-clockwise of the current marble.
		for i in range(0, 7):
			marble = marble.prev

		before = marble.prev
		after = marble.next

		before.next = after
		after.prev = before

		self.current = after

		return marble.value

# Plays the elf marble game. Returns the winning score
def playGame(player_count, last_marble):
	
	# Initialize the players
	current_player = Player()
	player = current_player
	for _ in range(0, player_count - 1):
		player.next = Player()
		player = player.next
	player.next = current_player

	marble = 0
	marbles = Marbles(marble)

	while marble < last_marble:
		marble += 1
		current_player = current_player.next

		if marble % special == 0:
			current_player.points += marbles.popMarble() + marble
		else:
			marbles.pushMarble(marble)

	# Calculate the winning score.
	max_score = current_player.points
	for _ in range(0, player_count):
		current_player = current_player.next
		if current_player.points > max_score:
			max_score = current_player.points

	return max_score

player_count = 465
winning_score_part1 = 71940
winning_score_part2 = winning_score_part1 * 100

# Play the elf marble game
part1_score = playGame(player_count, winning_score_part1)

# Play the elf marble game with x100 more marbles than part 1.
part2_score = playGame(player_count, winning_score_part2)

print("Part 1 score: " + str(part1_score))
print("Part 2 score: " + str(part2_score))
