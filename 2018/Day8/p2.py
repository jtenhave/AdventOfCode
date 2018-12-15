import c

# Parse a tree of nodes. Comput the 'value' (see c1.py) of the root node.

root = c.parseTreeFile("i1.txt")
value = root.getValue()

print(value)
