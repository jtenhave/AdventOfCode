import re

pattern = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

# A step that depends on other steps and has other steps depending on it.
class Step:
	def __init__(self, id):
		self.id = id
		self.before = set()
		self.after = set()
		self.done = False
		self.remaining = ord(id) - 4 # Each letter takes 60 seconds plus its position in the alphabet. 'A' takes 61, or 65 - 4

	def addBefore(self, step):
		self.before |= { step }

	def addAfter(self, step):
		self.after |= { step }

	def isReady(self):
		return len(list(filter(lambda s: not s.done, self.before))) == 0

# Parse a file with steps in it.
def parseStepFile(file):
	with open(file) as input:
		lines = input.readlines()

	steps = {}

	for line in lines:
		m = pattern.match(line)

		id_a = m[1]
		id_b = m[2]

		if id_a not in steps:
			steps[id_a] = Step(id_a)

		if id_b not in steps:
			steps[id_b] = Step(id_b)	

		stepA = steps[id_a]
		stepB = steps[id_b]

		stepB.addBefore(stepA)
		stepA.addAfter(stepB)

	return steps.values()
