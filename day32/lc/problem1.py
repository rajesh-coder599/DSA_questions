# 2126. Destroying Asteroids


def asteroidsDestroyed(mass,asteroids):
    asteroids.sort()
    for i in asteroids:
        if i>mass:
            return False
        else:
            mass+=i
    return True