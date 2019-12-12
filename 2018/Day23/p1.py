import c

nanobots = c.parseNanobotFile("i1.txt")

longest_range = max(nanobots, key=lambda n: n.r)

in_range = 0
for nanobot in nanobots:
	distance = longest_range.distance(nanobot)

	if distance <= longest_range.r:
		in_range += 1

print(in_range)
