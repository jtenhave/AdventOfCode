import c

firstGen = "#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#."

# Part 1 - 20 Generations
pots = c.parseFile("i1.txt", firstGen)
for _ in range(0, 20):
	pots.advanceGeneration()

total = pots.computeTotal()
print(total)


# Part 2 - 50B Generations.
pots = c.parseFile("i1.txt", firstGen)

last_gen = firstGen
last_total = pots.computeTotal();
for i in range(1, 50000001):

	# Assume that the pots will stablize after a certain number of generations. Check for stablization every thousand generations.
	for j in range(1, 1001):
		pots.advanceGeneration()

	current_gen = pots.toString();
	if current_gen == last_gen:
		current_total = pots.computeTotal()
		increase_per_kilo_generation = current_total - last_total
		kilo_generations_left = 50000000 - i;

		print(current_total + (increase_per_kilo_generation * kilo_generations_left))
		exit()
	else:
		last_gen = current_gen
		last_total =  pots.computeTotal()
		