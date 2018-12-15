import c
import itertools

# Parse a list of steps that depend on other steps. If two steps can be completed at the same time,
# the one with the lower id comes first. Each steps takes a certain number of seconds to complete.
# There are 5 workers who can work on steps in parallel.

steps = c.parseStepFile("i1.txt")
ready = list(filter(lambda s: len(s.before) == 0, steps))
in_progress = []
finished = []

workers = 5
time = 0

while True:

	# Check for steps that are finished and put workers back in the pool.
	for step in in_progress:
		if step.remaining == 0:
			step.done = True
			finished.append(step)
			in_progress.remove(step)
			workers += 1

			new_ready = filter(lambda s: s.isReady(), step.after)
			for step in new_ready:
				if step not in ready:
					ready.append(step)

	# Check if we are done.
	if len(finished) == len(steps):
		break

	# Prepare the list of steps that are ready.
	if len(ready) != 1:
		ready.sort(key=lambda s: s.id)

	# Assign steps to idle workers.
	while workers > 0 and len(ready) > 0:
		step = ready.pop(0)
		in_progress.append(step)
		workers -= 1

	min_time_left = min(in_progress, key=lambda s: s.remaining).remaining

	# Take time off steps in progress.
	for step in in_progress:
		step.remaining -= min_time_left

	time += min_time_left

print(time)