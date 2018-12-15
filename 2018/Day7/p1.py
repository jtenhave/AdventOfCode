import c
import itertools

# Parse a list of steps that depend on other steps. If two steps can be completed at the same time,
# the one with the lower id comes first.

steps = c.parseStepFile("i1.txt")
ready = list(filter(lambda s: len(s.before) == 0, steps))
finished = []

while len(finished) != len(steps):
	if len(ready) != 1:
		ready.sort(key=lambda s: s.id)

	# Do the first step that is ready.
	next_step = ready.pop(0)
	next_step.done = True
	finished.append(next_step)

	# Find steps that are now ready.
	new_ready = filter(lambda s: s.isReady(), next_step.after)
	for step in new_ready:
		if step not in ready:
			ready.append(step)
	
print("".join(list(map(lambda s: s.id, finished))))
