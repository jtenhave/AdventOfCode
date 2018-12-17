import c

grid_serial_num = 7689

# Part 1: Find the maximum sum of values in any 3x3 sub grid of the main grid.
part1Result = c.findMaxPowerLevel(grid_serial_num, [3])
print(part1Result)

# Part 1: Find the maximum sum of values in any NxN sub grid of the main grid.
part2Result = c.findMaxPowerLevel(grid_serial_num, list(range(3, 301)))
print(part2Result)
