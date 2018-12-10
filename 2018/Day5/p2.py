import c
import operator

# Read in a list of characters. See which character will result on the shortest "reacted" string (see part 1) when removed. 

def allChars():
    for c in range(ord('a'), ord('z') + 1):
        yield chr(c)

with open("i1.txt") as input:
    polymer = list(input.read())

c.react(polymer)

lengths = {}
for char in allChars():
	newpolymer = list(filter(lambda x: x.lower() != char, polymer.copy()))
	c.react(newpolymer)
	lengths[char] = len(newpolymer)

print(min(lengths.items(), key=operator.itemgetter(1))[1])
