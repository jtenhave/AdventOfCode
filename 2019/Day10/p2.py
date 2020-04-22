import c

# Compute the slope of a line.
def slope(rise, run):

    if run == 0:
        return float("inf") if rise > 0 else float("-inf")
    
    return rise / run

# Load the asteroid field.
asteroidField = c.loadAsteroidField("i1.txt")

# Asteroid with the laser on it.
laserAsteroid = asteroidField.asteroidMap[29][26]

# Vaporize an asteroid.
vaporized = 0
def vaporize(bisection):
    global vaporized

    slopes = sorted(set(map(lambda s: s[2] , bisection)))

    for slope in slopes:

        # Find the closest asteroid.
        asteroid = sorted(list(filter(lambda s: s[2] == slope, bisection)), key=lambda s: abs(s[0]) + abs(s[1]))[0][3]
        asteroidField.vaporize(asteroid)
        vaporized += 1
        if vaporized == 200:
            print(asteroid.x * 100 + asteroid.y)
            exit()

while True:
    deltas = []
    for asteroid in asteroidField.asteroids:
        if asteroid == laserAsteroid:
            continue
        
        deltaX = asteroid.x - laserAsteroid.x
        deltaY = asteroid.y - laserAsteroid.y

        deltas.append((deltaX, deltaY, slope(deltaY, deltaX), asteroid))

    rightBisection = list(filter(lambda s: s[0] >= 0, deltas))
    vaporize(rightBisection)

    leftBisection = list(filter(lambda s: s[0] < 0, deltas))
    vaporize(leftBisection)




