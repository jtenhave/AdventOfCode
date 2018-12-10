def doReact(a, b):
	if a.lower() != b.lower():
		return False

	if a.isupper() and b.isupper():
		return False

	if a.islower() and b.islower():
		return False

	return True

# Remove all pairs of chars that are the same with opposite capitalization.
def react(polymer): 
	i = 0
	while i < len(polymer) - 1:
		a = polymer[i]
		b = polymer[i + 1]

		if doReact(a, b):
			del polymer[i]
			del polymer[i]
			if i != 0:
				i -= 1
		else:
			i += 1