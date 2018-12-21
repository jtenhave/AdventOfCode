import re

pattern = re.compile("([#\.]{5}) => ([#\.])")

bin_values = [2**4, 2**3, 2**2, 2**1, 2**0]

# A pot that might have a plant in it.
class Pot:
	def __init__(self, index, hasPlant):
		self.index = index
		self.hasPlant = hasPlant
		self.next = None

# A row of pots that extends infinitely in either direction
class PotList:
	def __init__(self, hasPlant, nextGenCodes):
		pot = Pot(0, hasPlant)
		self.head = pot
		self.tail = pot
		self.nextGenCodes = nextGenCodes

	# Add pot to the right end of the pot row.
	def addPotAtTail(self, hasPlant):
		pot = Pot(self.tail.index + 1, hasPlant)
		self.tail.next = pot
		self.tail = pot
	
	# Add pot ti the left end of the pot row.
	def addPotAtHead(self, hasPlant):
		pot = Pot(self.head.index - 1, hasPlant)
		pot.next = self.head
		self.head = pot

	# Move to the next generation of plants.
	def advanceGeneration(self):
		# Compute the initial int value
		int_code = self.head.hasPlant << 1
		int_code += self.head.next.hasPlant
		
		next_pot = self.head;

		# Check if we need add a pot at the head of the list.
		if int_code in self.nextGenCodes:
			self.addPotAtHead(1)
		else:
			# Extract the first iteration so we can keep the head of the list pruned and avoid uncessary operations
			int_code = (int_code & 15) << 1;
			int_code += next_pot.next.next.hasPlant
			if int_code in self.nextGenCodes:
				next_pot.hasPlant = 1
			else:
				self.head = next_pot.next

			next_pot = next_pot.next

		# The main loop.
		while next_pot.next.next is not None:
			int_code = (int_code & 15) << 1;
			int_code += next_pot.next.next.hasPlant
			next_pot.hasPlant = 1 if int_code in self.nextGenCodes else 0
			next_pot = next_pot.next

		# Extract the last two loop iterations to avoid trillions (literally) of IF checks
		int_code = (int_code & 15) << 1;
		next_pot.hasPlant = 1 if int_code in self.nextGenCodes else 0
		next_pot = next_pot.next

		int_code = (int_code & 15) << 1;
		next_pot.hasPlant = 1 if int_code in self.nextGenCodes else 0
		next_pot = next_pot.next

		# Check if we need add a pot at the tail of the list.
		int_code = (int_code & 15) << 1;
		if int_code in self.nextGenCodes:
			self.addPotAtTail(1)

	# Compute the total value of plants in the row.
	def computeTotal(self):
		total = 0
		next_pot = self.head
		while next_pot is not None:
			total += next_pot.index if next_pot.hasPlant else 0
			next_pot = next_pot.next

		return total

	# Return string value of the pot row.
	def toString(self):
		code = ""
		next_pot = self.head
		while next_pot is not None:
			code += "#" if next_pot.hasPlant else "."
			next_pot = next_pot.next

		return code

# Create an int from a generation code.
def toInt(code):
	value = 0
	for i, code in enumerate(code):
		if hasPlant(code):
			value += bin_values[i]
	return value

# Whether a pot code indicates there is a plant.
def hasPlant(code):
	return code == "#" or code == '#'

# Parse a file containing pot generation information.
def parseFile(file, firstGen):
	with open(file) as input:
		lines = input.readlines()

	nextGenCodes = set()
	for line in lines:
		m = pattern.match(line.strip())
		if hasPlant(m.group(2)):
			nextGenCodes.add(toInt(m.group(1)))

	pots = PotList(hasPlant(firstGen[0]), nextGenCodes)
	for i in range(1, len(firstGen)):
		pots.addPotAtTail(hasPlant(firstGen[i]))

	return pots
