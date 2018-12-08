# Read char sequences from a text file. Count the number of sequences that repeat the same character 
# two or three times. Compute the product of these counts.

with open("i1.txt") as input:
	lines = input.readlines()

twos = 0;
threes = 0;

for line in lines:
	counts = {}
	for c in line:
		if not c in counts:
			counts[c] = 0
		counts[c] += 1

	counts = list(counts.values())
	if 2 in counts:
		twos += 1

	if 3 in counts:
		threes += 1

print(twos * threes)