
# Class that represents an asteroid field.
class AsteroidField:
    def __init__(self):
        self.asteroids = []
        self.asteroidMap = []
    
    # Vaporize an asteroid in the asteroid field.
    def vaporize(self, asteroid):
        self.asteroids.remove(asteroid)
        self.asteroidMap[asteroid.y][asteroid.x] = None

# Class that represents an asteroid.
class Asteroid:
    def __init__(self, x, y):
        self.visible = None
        self.x = x
        self.y = y

    # Remove another asteroid from the list of visible asteroids.
    def removeVisible(self, asteroid):
        if asteroid in self.visible:
            self.visible.remove(asteroid)
            asteroid.visible.remove(self)

# Load the asteroid field data from a file.
def loadAsteroidField(file):

    # Read data from a text file.
    with open(file) as input:
        lines = input.readlines()

    asteroidField = AsteroidField()
    for y, line in enumerate(lines):

        asteroidField.asteroidMap.append([])

        for x, char in enumerate(line):

            if char == "#":
                asteroid = Asteroid(x, y)
                asteroidField.asteroids.append(asteroid)
                asteroidField.asteroidMap[-1].append(asteroid)

            if char == ".":
                asteroidField.asteroidMap[-1].append(None)
    
    # Add every other asteroid to the list of visible asteroids.
    for asteroid in asteroidField.asteroids:
        asteroid.visible = asteroidField.asteroids.copy()
        asteroid.visible.remove(asteroid)

    return asteroidField

        