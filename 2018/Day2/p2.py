# Read char sequences from a text file. Find the two sequences that differ by only one char
# and print the common parts of the sequence.

with open("i1.txt") as input:
	lines = input.readlines()

for i, idA in enumerate(lines):
	for _, idB in enumerate(lines, i + 1):
		diff = -1;
		for k, c in enumerate(idA):
			if c != idB[k]:
				if diff >= 0:
					diff = -1
					break
				diff = k

		if diff >= 0:
			print(idA[:diff] + idA[diff + 1:])
			exit()

