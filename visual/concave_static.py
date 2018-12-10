import hull
from pyprocessing import *
from random import randint

HEIGHT = 500
WIDTH = 1000
COUNT = 100
OFFSET = 25
SIZE = 5


def setup():
    """Initial setup function."""
    size(WIDTH, HEIGHT)
    background(255)
    fill(0)
    stroke(0)

    points = [] 
        for i in range(COUNT):
        x = randint(OFFSET, WIDTH - OFFSET)
        y = randint(OFFSET, HEIGHT - OFFSET)
        points.append((x, y))
        ellipse(x, y, SIZE, SIZE)

    concave = hull.concave(points)
    for i in range(len(concave) - 1):
        line(concave[i], concave[i + 1])
    line(concave[-1], concave[0])


run()
