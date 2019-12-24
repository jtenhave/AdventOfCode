import re

orbitPattern = re.compile("(\w*)\)(\w*)")

# Class that represents an orbiting object.
class Object:
    def __init__(self, id):
        self.id = id
        self.parent = None

    # Total number of orbits this object has around the central mass.
    def totalOrbits(self):
        if not self.parent:
            return 0
        else:
            return 1 + self.parent.totalOrbits()

# Get the objects.
def getObjects(file):

    with open(file) as input:
        orbitDefs = input.readlines()

    objects = {}

    for orbitDef in orbitDefs:
        match = orbitPattern.match(orbitDef)
        parentID = match[1]
        childID = match[2]

        if parentID not in objects:
            objects[parentID] = Object(parentID)
        
        if childID not in objects:
            objects[childID] = Object(childID)

        parent = objects[parentID]
        child = objects[childID]

        child.parent = parent

    return objects
