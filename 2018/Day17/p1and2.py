import c

scan = c.parseScanFile("i1.txt")
scan.flood()

# Part 1: Find the number of squares that ever get wet.
# Part 2: Find the number of squares that retain water.

wet = 0
water = 0
for row in scan.squares:
	for square in row:
		if square.wet:
			wet += 1

		if square.water:
			water += 1

print(wet)
print(water)
