import c

facility = c.parseFacilityFile("i1.txt")

# Part 1. Find the farthest room
farthest = max(facility.rooms, key=lambda r: r.distance)
print(farthest.distance)

# Part 2. Find the number of rooms that more than 1000 doors away.
rooms = list(filter(lambda r: r.distance >= 1000, facility.rooms))
print(len(rooms))