import random
from hull import *
from pyprocessing import *

# Configuration
HEIGHT = 500
WIDTH = 1000
COUNT = 200
OFFSET = 10
SIZE = 5

points = list()
for i in range(0, COUNT):
    points.append((random.randint(OFFSET, WIDTH - OFFSET), random.randint(OFFSET, HEIGHT - OFFSET)))

border = concave_hull(points, 3)


def setup():
    size(WIDTH, HEIGHT)
    background(0)
    for p in points:
        ellipse(p[0], p[1], SIZE, SIZE)

    for i in range(0, len(border) - 1):
        stroke(255)
        line(border[i], border[i + 1])


run()
