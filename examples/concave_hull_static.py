from hull import *
from pyprocessing import *
from random import randint

# Configuration
HEIGHT = 500
WIDTH = 1000
COUNT = 200
OFFSET = 25
SIZE = 5


def setup():
    size(WIDTH, HEIGHT)
    background(0)
    fill(255)
    stroke(255)

    points = []  # List of points
    for i in range(0, COUNT):
        x, y = randint(OFFSET, WIDTH - OFFSET), randint(OFFSET, HEIGHT - OFFSET)
        points.append((x, y))
        ellipse(x, y, SIZE, SIZE)

    c_hull = concave_hull(points, 3)  # Calculate concave hull
    for i in range(0, len(c_hull) - 1):
        line(c_hull[i], c_hull[i + 1])
    line(c_hull[-1], c_hull[0])  # Close hull


run()
