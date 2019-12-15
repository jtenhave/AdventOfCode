import c

# Read the the wire definition from the input file.
with open("i1.txt") as input:
    wires = input.readlines()

wireDefA = wires[0].split(",")
wireDefB = wires[1].split(",")

wireA = c.getWire(wireDefA)
wireB = c.getWire(wireDefB)

shortestDistance = float("Inf")
shortestPath = float("Inf")

for a in wireA:
    for b in wireB:

        # Compare each section of wire.
        intersection = a.intersectionDistance(b)
        if (intersection):

            # Part 1: Look for the shortest Manhattan distance.
            if (intersection[0] < shortestDistance):
                shortestDistance = intersection[0]

            # Part2: Look for the shortest path.
            if (intersection[1] < shortestPath):
                shortestPath = intersection[1]

print (shortestDistance)
print (shortestPath)
