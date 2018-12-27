# An optimized python translation of the program in i1.txt

r0 = 0
r1 = 0
r3 = 0

values = set()
while True:
	r1 = r3 | 65536
	r3 = 9450265

	while True:
		r3 += (r1 & 255)
		r3 &= 16777215 
		r3 *= 65899
		r3 &= 16777215

		if r1 < 256:

			# Part 1 - The first value printed
			# Part 2 - The last value printed.

			if r3 in values:
				exit()
			else:
				print(r3)
				values.add(r3)

			break

		# The main optimization - The inner loop just divides r1 by 256.
		r1 = r1 >> 8
