import c
import math

target_x = 5
target_y = 746
depth = 4002

# Get the common tool between neighboring regions.
def getCommonTool(region, neighbor):
	if region.type == c.rocky:
		if neighbor.type == c.wet:
			return c.climbing_gear
		else:
			return c.torch

	elif region.type == c.wet:
		if neighbor.type == c.rocky:
			return c.climbing_gear
		else:
			return c.neither

	elif region.type == c.narrow:
		if neighbor.type == c.rocky:
			return c.torch
		else:
			return c.neither

# Get the tool for region that is not the given tool.
def getOtherTool(region, tool):
	for t in region.getTools():
		if t != tool:
			return t

# Update a neighbor's distance for a given tool if possible.
def updateNeighborToolDistance(region, neighbor, tool):
	distance = region.distances[tool]
	if distance == math.inf:
		return False

	if distance + 1 < neighbor.distances[tool]:
		neighbor.distances[tool] = distance + 1
		return True

	return False

# Update a neighbor's distance for a tool switch if possible.
def updateNeighborToolDistanceWithSwitch(region, neighbor, start_tool, end_tool):
	distance = region.distances[start_tool]
	if distance == math.inf:
		return False

	if distance + 8 < neighbor.distances[end_tool]:
		neighbor.distances[end_tool] = distance + 8
		return True

	return False

# Update a neighbor's distance if possible.
def updateNeighborDistance(region, neighbor):
	if region == neighbor:
		return False

	# Check if the squares are the same
	if region.type == neighbor.type:
		updated_neighbor = 

		# Compare distances for all tools.
		for tool in region.getTools():
			updated_neighbor = updated_neighbor or updateNeighborToolDistance(region, neighbor, tool)
		return updated_neighbor
	else:
		common_tool = getCommonTool(region, neighbor)
		other_tool = getOtherTool(region, common_tool)

		common_distance = region.distances[common_tool]
		other_distance = region.distances[other_tool]

		if common_distance == math.inf:
			return updateNeighborToolDistanceWithSwitch(region, neighbor, other_tool, common_tool)
		elif other_distance == math.inf:
			return updateNeighborToolDistance(region, neighbor, common_tool)
		else:
			# If we have both tools, find the best possible distance.
			best_distance = min(other_distance + 8, common_distance + 1)
			if best_distance < neighbor.distances[common_tool]:
				neighbor.distances[common_tool] = best_distance
				return True

	return False

# Find the distances to regions in the cave.
def findDistancesToRegions(current):
	regions = [current]

	while len(regions) > 0:
		next_regions = []
		for region in regions:
			for neighbor in region.getNeighbors():
				neighbor_updated = updateNeighborDistance(region, neighbor)
				if neighbor_updated:
					next_regions.append(neighbor)

		regions = next_regions


# Part 2 - Find the minimum distance to the target. 
(cave, risk) = c.createCave(target_x, target_y, depth, 100, 100)

target = cave.regions[target_y][target_x]
mouth = cave.regions[0][0]
mouth.distances[c.torch] = 0

findDistancesToRegions(mouth)

print(target.distances[c.torch])
