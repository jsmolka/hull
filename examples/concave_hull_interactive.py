from hull import *
from pyprocessing import *
from random import randint

# Configuration
HEIGHT = 500
WIDTH = 1000
SIZE = 5

# Define variables
points = []  # List of displayed points
c_hull = []  # Concave hull


def setup():
    size(WIDTH, HEIGHT)
    fill(255)
    stroke(255)
    background(0)


def mouseClicked():
    global points, c_hull
    background(0)  # Redraw background to delete old scenery
    points.append((mouse.x, mouse.y))
    for p in points:
        ellipse(p[0], p[1], SIZE, SIZE)
    if len(points) >= 3:
        c_hull = concave_hull(points, 3)
        for i in range(0, len(c_hull) - 1):
            line(c_hull[i], c_hull[i + 1])
        line(c_hull[-1], c_hull[0])  # Close hull


run()
