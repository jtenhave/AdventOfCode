import c

objects = c.getObjects("i1.txt")

# Calculate the total number of orbits.
totalOrbits = 0
for object in objects.values():
    totalOrbits += object.totalOrbits()

print(totalOrbits)
