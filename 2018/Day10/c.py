import re
import math

pattern = re.compile("position=<(.*), (.*)> velocity=<(.*), (.*)>")

# A light in the sky which has a position an velocity
class Light:
	def __init__(self, position, velocity):
		self.x = position[0]
		self.y = position[1]
		self.velocity = velocity

	# Update the current based on the velocity.
	def updatePosition(self):
		self.x = self.x + self.velocity[0]
		self.y = self.y + self.velocity[1]

# Update the postion of all the sky lights.
def advanceClock(lights):
	xmax = -math.inf
	xmin = math.inf
	ymax = -math.inf
	ymin = math.inf

	for light in lights:
		light.updatePosition()

		if light.x > xmax:
			xmax = light.x 
		if light.x < xmin:
			xmin = light.x
		if light.y > ymax:
			ymax = light.y
		if light.y < ymin:
			ymin = light.y

	return (xmax, xmin, ymax, ymin)

# Parse a file containing light positions and velocities.
def parseFile(file):
	with open(file) as input:
		lines = input.readlines()

	lights = []
	for line in lines:
		m = pattern.match(line)
		lights.append(Light((int(m.group(1)), int(m.group(2))),(int(m.group(3)), int(m.group(4)))))

	return lights

