import hull
from pyprocessing import *

HEIGHT = 500
WIDTH = 1000
SIZE = 5

points = []
convex = []


def setup():
    """Initial setup function."""
    size(WIDTH, HEIGHT)
    fill(0)
    stroke(0)
    background(255)


def mouseClicked():
    """Mouse click event function."""
    global points, convex
 
    background(255)
    points.append((mouse.x, mouse.y))
 
    for p in points:
        ellipse(p[0], p[1], SIZE, SIZE)
 
    if len(points) >= 3:
        convex = hull.convex(points)
        for i in range(len(convex) - 1):
            line(convex[i], convex[i + 1])
        line(convex[-1], convex[0])


run()
