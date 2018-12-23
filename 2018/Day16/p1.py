import re
import ast
import c

pattern = re.compile("Before: (.*)\n(\d*) (\d*) (\d*) (\d*)\nAfter: (.*)")

# Read the samples from the file.
with open("i1.txt") as input:
	data = input.read()

samples = re.findall(pattern, data)

# Find the number of sameples that match 3 or more op codes
matches_three = 0
for sample in samples:
	before = ast.literal_eval(sample[0].strip())
	operand1 = int(sample[2])
	operand2 = int(sample[3])
	rd = int(sample[4])
	after = ast.literal_eval(sample[5].strip())

	matches = 0
	for op in c.all_ops:
		processor = c.Processor()
		processor.loadRegisters(before)
		processor.execute(op, operand1, operand2, rd)
		
		if processor.registers == after:
			matches += 1

		if matches >= 3:
			matches_three +=1
			break;

print(matches_three)
