import c

# Read in a list of characters. Remove all pairs that are the same letter with opposite capitalization.
with open("i1.txt") as input:
    polymer = list(input.read())

c.react(polymer)

print(len(polymer))
