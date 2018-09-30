import hull
from pyprocessing import *
from random import randint

# Configuration
HEIGHT = 500
WIDTH = 1000
COUNT = 100
OFFSET = 25
SIZE = 5


def setup():
    """
    Setup.

    :return: None
    """
    size(WIDTH, HEIGHT)
    background(255)
    fill(0)
    stroke(0)

    points = []  # List of points
    for i in range(COUNT):
        x, y = randint(OFFSET, WIDTH - OFFSET), randint(OFFSET, HEIGHT - OFFSET)
        points.append((x, y))
        ellipse(x, y, SIZE, SIZE)

    c_hull = hull.convex(points)  # Calculate convex hull
    for i in range(len(c_hull) - 1):
        line(c_hull[i], c_hull[i + 1])
    line(c_hull[-1], c_hull[0])  # Close hull


run()
