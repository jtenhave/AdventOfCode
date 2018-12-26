
# A processor that executes operations.
class Processor:

	def __init__(self):
		self.registers = [0,0,0,0,0,0]
		self.ip = 0
		self.ip_r = None;
		self.program = None
		self.ops = { "addr": self.addr, "addi": self.addi, "mulr": self.mulr, "muli": self.muli, "banr": self.banr, "bani": self.bani, "borr": self.borr, "bori": self.bori, "setr": self.setr, "seti": self.seti, "gtir": self.gtir, "gtri": self.gtri, "gtrr":self.gtrr, "eqir": self.eqir, "eqri": self.eqri, "eqrr": self.eqrr}

	def loadProgram(self, program, ip_r):
		self.ip_r = ip_r
		self.program = program

	# Executes the loaded program.
	def executeProgram(self):
		while True:

			# Halt execution if the instruction pointer is out of range.
			if self.ip >= len(self.program):
				return

			# Get the next instruction.
			instruction = self.program[self.ip]

			# Load the instruction pointer into the bound register.
			self.registers[self.ip_r] = self.ip

			# Execute the instruction
			op = self.ops[instruction[0]]
			result = op(instruction[1], instruction[2])
			self.registers[instruction[3]] = result

			# Write the value of the bound register to the instruction pointer.
			self.ip = self.registers[self.ip_r] + 1

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
