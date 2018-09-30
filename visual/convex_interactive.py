import hull
from pyprocessing import *
from random import randint

# Configuration
HEIGHT = 500
WIDTH = 1000
SIZE = 5

# Define variables
points = []  # List of displayed points
c_hull = []  # Convex hull


def setup():
    """
    Setup.

    :return: None
    """
    size(WIDTH, HEIGHT)
    fill(0)
    stroke(0)
    background(255)


def mouseClicked():
    """
    Mouse clicked event.

    :return: None
    """
    global points, c_hull
    background(255)  # Redraw background to delete old scenery
    points.append((mouse.x, mouse.y))
    for p in points:
        ellipse(p[0], p[1], SIZE, SIZE)
    if len(points) >= 3:
        c_hull = hull.convex(points)  # Calculate convex hull
        for i in range(len(c_hull) - 1):
            line(c_hull[i], c_hull[i + 1])
        line(c_hull[-1], c_hull[0])  # Close hull


run()
