
all_ops = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

# A processor that executes operations.
class Processor:

	def __init__(self):
		self.registers = [0,0,0,0]

	# Loads values into the registers.
	def loadRegisters(self, values):
		for i, v in enumerate(values):
			self.registers[i] = v

	# Executes an operation.
	def execute(self, name, operand1, operand2, rd):
		op = getattr(self, name)
		result = op(operand1, operand2)
		self.registers[rd] = result

	# Adds register operand1 to register operand2.
	def addr(self, operand1, operand2):
		return self.registers[operand1] + self.registers[operand2]

	# Adds register operand1 to value operand2.
	def addi(self, operand1, operand2):
		return self.registers[operand1] + operand2

	# Multiplies register operand1 by register operand2.
	def mulr(self, operand1, operand2):
		return self.registers[operand1] * self.registers[operand2]

	# Multiplies register operand1 by value operand2.
	def muli(self, operand1, operand2):
		return self.registers[operand1] * operand2

	# Bitwise AND of register operand1 and register operand2.
	def banr(self, operand1, operand2):
		return self.registers[operand1] & self.registers[operand2]

	# Bitwise AND of register operand1 and value operand2.
	def bani(self, operand1, operand2):
		return self.registers[operand1] & operand2

	# Bitwise OR of register operand1 and register operand2.
	def borr(self, operand1, operand2):
		return self.registers[operand1] | self.registers[operand2]

	# Bitwise OR of register operand1 and value operand2.
	def bori(self, operand1, operand2):
		return self.registers[operand1] | operand2

	# Return the value of register operand1.
	def setr(self, operand1, operand2):
		return self.registers[operand1]

	# Return the value of operand1.
	def seti(self, operand1, operand2):
		return operand1

	# GT of value operand1 and register operand2
	def gtir(self, operand1, operand2):
		return 1 if operand1 > self.registers[operand2] else 0

	# GT of register operand1 and value operand2
	def gtri(self, operand1, operand2):
		return 1 if self.registers[operand1] > operand2 else 0

	# GT of register operand1 and register operand2
	def gtrr(self, operand1, operand2):
		return 1 if self.registers[operand1] > self.registers[operand2] else 0

	# Compare value operand1 and register operand2
	def eqir(self, operand1, operand2):
		return 1 if operand1 == self.registers[operand2] else 0

	# Compare register operand1 and value operand2
	def eqri(self, operand1, operand2):
		return 1 if self.registers[operand1] == operand2 else 0

	# Compare register operand1 and register operand2
	def eqrr(self, operand1, operand2):
		return 1 if self.registers[operand1] == self.registers[operand2] else 0
