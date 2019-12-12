import math

# Read module masses from a text file.
with open("i1.txt") as input:
	lines = input.readlines()

# Calculate fuel.
def calculateFuel(mass):
	fuel = math.floor(mass / 3) - 2
	if (fuel <= 0):
		return 0
	
	return fuel + calculateFuel(fuel)


# Part 2. Calculate the total fuel taking in account the fuel itself.
totalFuel = 0
for line in lines:
	mass = int(line)
	totalFuel += calculateFuel(mass)

print(totalFuel);
