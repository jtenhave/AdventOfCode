import math

# Read module masses from a text file.
with open("i1.txt") as input:
	lines = input.readlines()

# Part 1. Calculate the total fuel.
totalFuel = 0
for line in lines:
	mass = int(line)
	totalFuel += math.floor(mass / 3) - 2

print(totalFuel);
