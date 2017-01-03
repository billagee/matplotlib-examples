#!/usr/bin/env python3.5

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import golden

def plot_equilateral_triangle(sidelength, startx=0, starty=0):
    # Find equilateral triangle height by halving it and finding the long side
    # of the resulting right triangle.
    # See Google pythagorean calc search:
    #   a = sqrt(c^2 - b^2)
    #   pythagorean theorem calc: find a, b=n/a, c=n/a
    #   https://www.google.com/search?q=pythagorean+theorem+calc%3A+find+a%2C+b%3Dn%2Fa%2C+c%3Dn%2Fa
    height = np.sqrt([ sidelength**2 - (sidelength / 2.0) ])[0]

    # x1,y1 is the left vertex of the triangle, x2,y2 the right, x3,y3 the top
    x1 = startx
    y1 = starty
    x2 = startx + sidelength
    y2 = starty
    x3 = startx + (sidelength / 2.0)
    y3 = starty + height
    ax.plot(np.array([x1, x2, x3, x1]), np.array([y1, y2, y3, y1]))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)

# Put left vertex of first triangle at coords 1,1:
len_orig = 21
startx = 0
starty = 0
for i in range(0, 3):
    plot_equilateral_triangle(len_orig / golden, startx, starty)
    startx += 1
    starty += 1

plt.show()
