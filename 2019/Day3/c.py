
# Parse a raw wire defintion and return the wire sections
def getWire(wireDef):

    wire = []

    start = (0, 0)
    offset = 0;

    for endDef in wireDef:
        
        dir = endDef[0]
        mag = int(endDef[1:])

        end = None
        if (dir == "R"):
            end = (start[0] + mag, start[1])
        if (dir == "L"):
            end = (start[0] - mag, start[1])
        if (dir == "U"):
            end = (start[0], start[1] + mag)
        if (dir == "D"):
            end = (start[0], start[1] - mag)
        
        wire.append(Section(start, end, offset))
        
        start = end
        offset += mag

    return wire


# A section of wire.
class Section:
    def __init__(self, start, end, offset):
        self.sX = start[0]
        self.sY = start[1]
        self.eX = end[0]
        self.eY = end[1]
        self.offset = offset
        self.isVertical = self.sX == self.eX

    # Get the intersection of two wire sections.
    def intersectionDistance(self, section):

        # Check if the wire sections can possibly intersect.
        if self.isVertical == section.isVertical:
            return None

        vertical = self if self.isVertical else section
        horizontal = section if self.isVertical else self

        # Check for Y intersection.
        if horizontal.sY <= min(vertical.sY, vertical.eY) or horizontal.sY >= max(vertical.sY, vertical.eY):
            return None

        # Check for X intersection.
        if vertical.sX <= min(horizontal.sX, horizontal.eX) or vertical.sX >= max(horizontal.sX, horizontal.eX):
            return None

        steps = self.offset + section.offset + abs( horizontal.sY - vertical.sY) + abs(vertical.sX - horizontal.sX)

        return (abs(vertical.sX) + abs(horizontal.sY), steps)
