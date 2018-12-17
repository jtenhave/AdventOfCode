import re

width = 300
height = 300

pattern = re.compile("\d{0,9}(\d)\d\d$")

# A fuel cell in the grid.
class FuelCell:
	def __init__(self, x, y, serial_number):
		self.power_level = self.computePowerLevel(x, y, serial_number)
		self.left = None
		self.right = None
		self.below = None
		self.x = x
		self.y = y

	def computePowerLevel(self, x, y, serial_number):
		# Calulate the 'power level' of the cell using the formula.
		rackId = x + 10
		power_level = rackId * y
		power_level += serial_number
		power_level *= rackId

		m = pattern.match(str(power_level))
		if m is None:
			power_level = 0
		else:
			power_level = int(m.group(1)) - 5

		return power_level;

# An NxN grid of fuel cells. This is a linked list where each fuel cell is linked
# to the cells to the left and right, and the cell below it.
class FuelCellGrid:

	def __init__(self, width, height, serial_number):
		self.serial_number = serial_number
		self.initalize(width, height)

	# Initialize the grid
	def initalize(self, width, height):

		# Initialize the first row
		row_head = self.initializeRow(width, 1, None);
		self.head = row_head;

		# Initialize the rest of the rows
		for y in range(2, height + 1):
			row_head = self.initializeRow(width, y, row_head)

	# Initialize a row of fuel cells in the grid.
	def initializeRow(self, width, y,  above):
		current_cell = FuelCell(1, y, self.serial_number)
		above = self.linkAboveCell(current_cell, above)
		first = current_cell

		for x in range(2, width + 1):
			new_cell = FuelCell(x, y, self.serial_number)

			# Set up the cell links.
			current_cell.right = new_cell
			new_cell.left = current_cell
			above = self.linkAboveCell(new_cell, above)

			current_cell = new_cell

		return first

	# Set the link with the cell above. Return the cell that will be above the cell to the right.
	def linkAboveCell(self, cell, above):
		if above is not None:
			above.below = cell
			return above.right

# A column of fuel cells in the sub-grid.
class Column:
	def __init__(self, height, head):
		self.top = head
		self.bottom = head
		self.power_level = head.power_level
		for _ in range(1, height):
			self.bottom = self.bottom.below
			self.power_level += self.bottom.power_level

	# Shift the column down by one fuel cell.
	def shiftDown(self):
		if not self.canShiftDown():
			return 0 

		removed = self.top.power_level
		self.top = self.top.below
		self.bottom = self.bottom.below
		added = self.bottom.power_level

		# Compute the net power level change of the column
		change = added - removed
		self.power_level += change

		return change

	# Check if the column can be shifted down.
	def canShiftDown(self):
		return self.bottom.below is not None

# An NxN sub grid of the main grid. 
class Square:
	def __init__(self, width, height, head):
		self.columns = []
		self.used_columns = []
		self.next_columns = []
		self.height = height
		self.width = width
		self.power_level = 0

		# Create the columns in the square
		column_head = head
		for _ in range (0, self.width):
			column = Column(self.height, column_head)
			self.power_level += column.power_level
			self.columns.append(column)
			column_head = column_head.right

	# Shift the square to the right by one column.
	def shiftRight(self):

		# Remove the tail column. Store it for the next time we move left.
		old_column = self.columns.pop(0)
		self.used_columns.append(old_column)

		# Find the next column. When moving right the column might not exist yet. If it exists, shift it down so 
		# its in the correct rows
		next_column = None
		if len(self.next_columns) > 0:
			next_column = self.next_columns.pop(0)
			next_column.shiftDown()
		else:
			next_column = Column(self.height, self.columns[-1].top.right)

		self.columns.append(next_column)

		# Comput the change in power level by remove a column and adding another.
		self.power_level -= old_column.power_level
		self.power_level += next_column.power_level

	# Shift the square to left by one column.
	def shiftLeft(self):

		# Remove the tail column and store it for next time we move right. 
		# When moving left, this will be at the end of the column list.
		old_column = self.columns.pop()
		self.used_columns.append(old_column)

		# Find the next column. When moving left, this will be at the end of the list.
		next_column = self.next_columns.pop()
		next_column.shiftDown()

		self.columns.insert(0, next_column)

		# Comput the change in power level by remove a column and adding another.
		self.power_level -= old_column.power_level
		self.power_level += next_column.power_level

	# Shift the square down. 
	def shiftDown(self):
		# Shift all columns down
		for column in self.columns:
			self.power_level += column.shiftDown()

		# Set the list of upcoming columns to the list of columns used in the last round.
		self.next_columns = self.used_columns
		self.used_columns = []

# Check if the max power level has changed. Return data associated with the max power level.
def checkMaxPowerLevel(square, size, powerLevelData):

	if powerLevelData is None or powerLevelData[3] < square.power_level:
		cell = square.columns[0].top
		return (cell.x, cell.y, size, square.power_level)

	return powerLevelData

# Find the maximum power level using a given number of sub-square sizes.
def findMaxPowerLevel(serial_number, sizes):

	# Setup the grid of cells.
	grid = FuelCellGrid(width, height, serial_number)
	max_power_level_data = None

	# Find the maximum sum of 'power levels' in any sized sub-grid of the main fuel cell grid.
	# With a grid size of 300x300 this will amount to a large number of computations, meaning we
	# need a strategy that will minimize the number of computations needed to calcuate the 
	# 'power level' sum for each sub grid

	# The idea is that we take the current sub-grid and shift if to left by one column until it reaches
	# the edge of main grid - calculating only the change in 'power level' value by adding one column
	# and removing another. When it reaches the edge of the main grid, we shift it down and move in 
	# opposite direction until we reach the other edge of the main grid.

	for size in sizes:
		square = Square(size, size, grid.head)
		move_right = True
		for _ in range(0, height - size):
			for _ in range(0, width - size):
				max_power_level_data = checkMaxPowerLevel(square, size, max_power_level_data)
				if move_right:
					square.shiftRight()
				else:
					square.shiftLeft()

			square.shiftDown()
			max_power_level_data = checkMaxPowerLevel(square, size, max_power_level_data)
			move_right = not move_right
		
	return max_power_level_data
