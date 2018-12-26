import re
import ast
import c

pattern = re.compile("(\w*) (\d*) (\d*) (\d*)")
ip_pattern = re.compile("#ip (\d)")

def readProgram(file):

	# Read and execute the program file.
	with open(file) as input:
		ip_line = input.readline()
		lines = input.readlines()

	m = ip_pattern.match(ip_line.strip())
	ip_r = int(m.group(1))

	program = []
	for line in lines:
		m = pattern.match(line.strip())
		op = m.group(1)
		operand1 = int(m.group(2))
		operand2 = int(m.group(3))
		rd = int(m.group(4))

		program.append((op, operand1, operand2, rd))

	return (program, ip_r)


(program, ip_r) = readProgram("i1.txt")

# Part 1 - Run the program.
processor = c.Processor()
processor.loadProgram(program, ip_r)
processor.executeProgram()
print(processor.registers)

(program, ip_r) = readProgram("i2.txt")

# Part 2 - Run the program with initial register value.
# The program finds the factors of a given number. Setting r1=1 will make the number very large.
# Added a slight optimization to the input program. Runs in ~20 minutes. Good enough!
processor = c.Processor()
processor.registers = [1, 0, 0,0,0,0]

#processor.registers[0] = 1
processor.loadProgram(program, ip_r)
processor.executeProgram()
print(processor.registers)
