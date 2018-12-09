import re
from datetime import datetime
from datetime import timedelta

# Class that represents a guard.
class Guard:
	def __init__(self, id):
		self.id = id
		self.totalSleepTime = 0
		self.sleepMinutes = dict.fromkeys(range(0, 60), 0)

	# Add sleep time for a guard.
	def addSleepTime(self, minutes):
		self.totalSleepTime += len(minutes)
		for minute in minutes:
			self.sleepMinutes[minute] += 1

linePattern = re.compile("\[(.*)\] (Guard #(\d{1,4}) begins shift)?(falls asleep)?")

# Parse the file that contains unordered guard log entries.
def parseGuards(file):
	with open(file) as input:
		lines = input.readlines()

	entries = list(map(lambda l: parseLine(l), lines))
	entries.sort(key=lambda l: l[0])

	guards = {}
	guard = None
	sleepStart = None
	for entry in entries:
		date = entry[0]
		id = entry[1]
		sleep = entry[2] is not None
		
		# Check if the guard has changed
		if id is not None:
			if id not in guards:
				guards[id] = Guard(id)
			guard = guards[id]
		elif sleep:
			sleepStart = date.minute
		else:
			guard.addSleepTime(range(sleepStart, date.minute))

	return guards.values()

# Parse a guard log entry.
def parseLine(line):
	m = linePattern.match(line)
	date = datetime.strptime(m.group(1) + "", '%Y-%m-%d %H:%M')

	# Ignore the minutes before midnight
	if date.hour != 0:
		date += timedelta(days=1)
		date = datetime(date.year, date.month, date.day, 0, 0)

	id = m.group(3)
	id = id if id is None else int(id)

	return (date, id, m.group(4))
