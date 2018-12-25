import c

area = c.parseCollectionArea("i1.txt")

# Part 1. Run for 10 minutes.
for _ in range(0, 10):
	area.advanceMinute()

print(area.computeResult())

# Part 2. Run for a billion minutes. Assume the pattern repeats. Check every thousandth minute.
area = c.parseCollectionArea("i1.txt")
results = []
for k in range(0, 1000000):
	for _ in range(0, 1000):
		area.advanceMinute()

	if len(results) == 0:
		results.append(area.computeResult())
	else:
		# Once values start repeating, calculate the final value.
		result = area.computeResult()
		if result == results[0]:
			cadence = len(results)
			i = 1000000 % ((cadence + 1) % cadence)
			print(str(results[i]))
			exit()
		else:
			results.append(result)
	