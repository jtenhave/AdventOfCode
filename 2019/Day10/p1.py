import c

# Load the asteroid data.
asteroidField = c.loadAsteroidField("i1.txt")

for i, asteroidA in enumerate(asteroidField.asteroids):

    for asteroidB in asteroidField.asteroids[i + 1:]:

        deltaX = asteroidB.x - asteroidA.x
        deltaY = asteroidB.y - asteroidA.y

        # Vertical line between asteroids.
        if deltaX == 0:
            y = asteroidA.y + deltaY
            while True:
                y += 1

                if y >= len(asteroidField.asteroidMap):
                    break
                
                asteroidC = asteroidField.asteroidMap[y][asteroidA.x]
                if asteroidC:
                    asteroidA.removeVisible(asteroidC)

        # Horizontal line between asteroids
        elif deltaY == 0:
            x = asteroidA.x + deltaX
            while True:
                x += 1 if deltaX > 0 else -1

                if x < 0 or x >= len(asteroidField.asteroidMap[asteroidA.y]):
                    break
                
                asteroidC = asteroidField.asteroidMap[asteroidA.y][x]
                if asteroidC:
                    asteroidA.removeVisible(asteroidC)

        # Diagonal line between asteroids.
        else:
            slope = deltaX/deltaY
            factor = 0

            while True:
                
                factor += 1

                nextX = asteroidB.x + (slope * factor )
                nextY = asteroidB.y + factor

                if nextY >= len(asteroidField.asteroidMap) or nextX < 0 or nextX >= len(asteroidField.asteroidMap[nextY]):
                    break

                if (not (nextX).is_integer()):
                    continue

                nextX = int(nextX)
                
                asteroidC = asteroidField.asteroidMap[nextY][nextX]
                if asteroidC:
                    asteroidA.removeVisible(asteroidC)

# Find the asteroid with the highest number of visible asteroids.
maxVisible = 0;
for asteroid in asteroidField.asteroids:
    if len(asteroid.visible) > maxVisible:
        maxVisible = len(asteroid.visible)

print(maxVisible)
