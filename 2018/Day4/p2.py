import c
import operator

# Find the sleepiest minute of any guard.

guards = c.parseGuards("i1.txt")
for guard in guards:
	guard.sleepiestMinute = max(guard.sleepMinutes.items(), key=operator.itemgetter(1))


sleepiestGuard = max(guards, key=lambda g: g.sleepiestMinute[1])

print(sleepiestGuard.id * sleepiestGuard.sleepiestMinute[0])