import c
import operator

# Find the sleepiest minute of the guard with the most total minutes asleep.

guards = c.parseGuards("i1.txt")
sleepiestGuard = max(guards, key=lambda g: g.totalSleepTime)
sleepiestMinute = max(sleepiestGuard.sleepMinutes.items(), key=operator.itemgetter(1))[0]

print(sleepiestGuard.id * sleepiestMinute)
