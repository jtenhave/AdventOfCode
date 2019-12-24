import c

objects = c.getObjects("i1.txt")

you = objects['YOU']
santa = objects['SAN']

# Find the common parent.
yourParents = []
yourParent = you.parent
while yourParent:
    yourParents.append(yourParent)
    yourParent = yourParent.parent

santaParent = santa.parent
while santaParent not in yourParents:
    santaParent = santaParent.parent

commonParent = santaParent

# Calculate the distance to santa
distance = you.parent.totalOrbits() + santa.parent.totalOrbits() - (2 * commonParent.totalOrbits())
print(distance) 
    