import c

# Parse a tree of nodes. Each node has numeric metadata. Compute the sum of all metadata in the tree.
root = c.parseTreeFile("i1.txt")

print(root.metadata_total)