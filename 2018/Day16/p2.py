import re
import ast
import c

sample_pattern = re.compile("Before: (.*)\n(\d*) (\d*) (\d*) (\d*)\nAfter: (.*)")
op_pattern = re.compile("(\d*) (\d*) (\d*) (\d*)")

# Track the possible codes for each op
possible_codes = {}
known_codes = {}
for op in c.all_ops:
	possible_codes[op] = list(range(0, len(c.all_ops)))

# Set a known code
def eliminateCode(op, op_code):

	if op_code not in possible_codes[op]:
		return

	possible_codes[op].remove(op_code)
	if len(possible_codes[op]) == 1:
		known_code = possible_codes[op][0]
		known_codes[known_code] = op
		for other_op in c.all_ops:
	 		eliminateCode(other_op, known_code)

# Read the samples from the file.
with open("i1.txt") as input:
	data = input.read()

# Determine the operation that matches each code.
samples = re.findall(sample_pattern, data)
for sample in samples:
	
	# Keep going if we already know what the op code maps to.
	op_code = int(sample[1])
	if op_code in known_codes:
		continue;

	before = ast.literal_eval(sample[0].strip())
	operand1 = int(sample[2])
	operand2 = int(sample[3])
	rd = int(sample[4])
	after = ast.literal_eval(sample[5].strip())

	for op in c.all_ops:
		# Keep going if we already know the code cannot map to this operation.
		if op_code not in possible_codes[op]:
			continue

		processor = c.Processor()
		processor.loadRegisters(before)
		processor.execute(op, operand1, operand2, rd)

		if processor.registers != after:
			eliminateCode(op, op_code)



# Read and execute the program file.
with open("i2.txt") as input:
	lines = input.readlines()

test_processor = c.Processor()
for line in lines:

	m = op_pattern.match(line)
	op_code = int(m.group(1))
	operand1 = int(m.group(2))
	operand2 = int(m.group(3))
	rd = int(m.group(4))

	op = known_codes[op_code]
	test_processor.execute(op, operand1, operand2, rd)

print(test_processor.registers)
