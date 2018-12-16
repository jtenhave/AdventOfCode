import c

lights = c.parseFile("i1.txt")

# Wait until the sky lights converge to a reasonable distance, tben advance one second at a time.
second = 0;
while True:

	result = c.advanceClock(lights)
	xmax = result [0]
	xmin = result[1]
	ymax = result[2]
	ymin = result[3]

	# Check if the lights have converged to a reasonable range.
	if xmax - xmin < 500 and ymax - ymin < 500:
		message = []
		for y in range(ymin, ymax + 1):
			message.append([])
			for x in range(xmin, xmax + 1):
				message[y - ymin].append(".")

		for light in lights:
			message[light.y - ymin][light.x - xmin] = "#"

		for row in message:
			print("".join(row))

		# Advance to the next second.
		input(str(second + 1) + " next...")

	second += 1
