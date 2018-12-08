# Read integers from a text file and sum until the same sum is reached twice.

with open("i1.txt") as input:
	lines = input.readlines()

freq = 0
freqs = { 0 }

while True:
	for line in lines:
		freq += int(line)
		if freq in freqs:
			print(freq)
			exit()
		
		freqs.add(freq)
