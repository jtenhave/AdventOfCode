
# A node in the tree.
class Node:
	def __init__(self):
		self.metadata = []
		self.metadata_total = 0
		self.children = []
		self.value = None

	# Add a child node.
	def addChild(self, child):
		self.children.append(child)

	# Add metadata.
	def addMetadata(self, metadata):
		self.metadata.append(metadata)
		self.metadata_total += metadata

    # Add metadata from a child.
	def addChildMetaDataTotal(self, metadata):
		self.metadata_total += metadata

	# Compute the value of a node. Value is defined as:
	# The sum of the node's metadata if it has no children OR
	# The sum of a subset of child node values. The subset is determined by the metadata which indicates the child indexes
	def getValue(self):
		if self.value is not None:
			return self.value

		child_count = len(self.children)
		if child_count == 0:
			self.value = sum(self.metadata)
		else:
			self.value = 0;
			for meta in self.metadata:
				if meta <= child_count:
					self.value += self.children[meta - 1].getValue()

		return self.value

# Parse a node from the tree.
def parseNode(iter):
	child_count = next(iter)
	metadata_count = next(iter)
	node = Node()
	for i in range(0, child_count):
		child = parseNode(iter)
		node.addChild(child)
		node.addChildMetaDataTotal(child.metadata_total)

	for i in range(0, metadata_count):
		metadata = next(iter)
		node.addMetadata(metadata)

	return node

# Parse a file that contains a tree of nodes.
def parseTreeFile(file):
	with open(file) as input:
		data = input.read()

	data = map(lambda i: int(i), data.split(" "))
	return parseNode(data)
