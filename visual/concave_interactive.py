import hull
from pyprocessing import *

HEIGHT = 500
WIDTH = 1000
SIZE = 5

points = []
concave = []


def setup():
    """Initial setup function."""
    size(WIDTH, HEIGHT)
    fill(0)
    stroke(0)
    background(255)


def mouseClicked():
    """Mouse click event function."""
    global points, concave
 
    background(255)
    points.append((mouse.x, mouse.y))
 
    for p in points:
        ellipse(p[0], p[1], SIZE, SIZE)
 
    if len(points) >= 3:
        concave = hull.concave(points)
        for i in range(len(concave) - 1):
            line(concave[i], concave[i + 1])
        line(concave[-1], concave[0])


run()
