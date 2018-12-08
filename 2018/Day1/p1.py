# Read integers from a text file and compute the sum.

with open("i1.txt") as input:
	lines = input.readlines()

sum = 0
for line in lines:
 sum += int(line)

print(sum)