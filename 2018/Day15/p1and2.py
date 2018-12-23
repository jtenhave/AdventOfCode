import c

# Part one - Play the game
game = c.parseGameFile("i1.txt", 3)
result =  game.play()
print(result)

# Part 2 - Increase elf attack until there are no elf casualties.
attack = 3
while True:
	game = c.parseGameFile("i1.txt", attack)
	elves = len(list(filter(lambda combatent: combatent.team == c.elf, game.combatents)))
	result = game.play()

	elves_remaining = len(list(filter(lambda combatent: combatent.team == c.elf, game.alive)))
	if elves == elves_remaining:
		print(result)
		exit()

	attack += 1
