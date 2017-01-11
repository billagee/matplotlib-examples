#!/usr/bin/env python3.5

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import golden

def plot_equilateral_triangle(
        sidelength, index=0, lastlines=None,
        hinge="right", invert=False):
    # Find equilateral triangle height by halving it and finding the long side # of the resulting right triangle.
    # See Google pythagorean calc search:
    #   a = sqrt(c^2 - b^2)
    #   pythagorean theorem calc: find a, b=n/a, c=n/a
    #   https://www.google.com/search?q=pythagorean+theorem+calc%3A+find+a%2C+b%3Dn%2Fa%2C+c%3Dn%2Fa
    height = np.sqrt([ sidelength**2.0 - (sidelength / 2.0) ])[0]

    # (x1,y1) is the triangle's left vertex, (x2,y2) the right, (x3,y3) the top
    startx = starty = None
    print("Plotting triangle {} starting at {} of old one".format(index, hinge))
    # Start points will always be third vertex plotted in prev triangle
    startx = lastlines[0].get_xdata()[2]
    starty = lastlines[0].get_ydata()[2]
    # Plot dot at start point
    #plt.plot([startx], [starty], 'ro')
    if hinge == "left":
        # Triangles started from left of prev get their vertexes
        # plotted in this order:
        # R -> L -> T
        if invert:
            x1 = startx + sidelength # right vertex
            y1 = starty # right
            x2 = startx # left
            y2 = starty # left
            x3 = startx + (sidelength / 2.0) # top
            y3 = starty - height # top
        else:
            x1 = startx # right vertex
            y1 = starty # right
            x2 = startx - sidelength # left
            y2 = starty # left
            x3 = startx - (sidelength / 2.0) # top
            y3 = starty + height # top
    elif hinge == "right":
        # Triangles started from right of prev get their vertexes
        # plotted in this order:
        # T -> R -> L
        if invert:
            x1 = startx # top
            y1 = starty # top
            x2 = startx - (sidelength / 2.0) # right
            y2 = starty + height # right
            x3 = startx + (sidelength / 2.0) # left
            y3 = starty + height # left
        else:
            x1 = startx # top
            y1 = starty # top
            x2 = startx + (sidelength / 2.0) # right
            y2 = starty - height # right
            x3 = startx - (sidelength / 2.0) # left
            y3 = starty - height # left
    elif hinge == "top":
        # Triangles started from top of prev get their vertexes
        # plotted in this order:
        # L -> T -> R
        #import pdb ; pdb.set_trace()
        if invert:
            x1 = startx # left
            y1 = starty # left
            x2 = startx - (sidelength / 2.0) # top
            y2 = starty - height # top
            x3 = startx - sidelength # right vertex
            y3 = starty # right
        else:
            x1 = startx # left
            y1 = starty # left
            x2 = startx + (sidelength / 2.0) # top
            y2 = starty + height # top
            x3 = startx + sidelength # right vertex
            y3 = starty # right
    else:
        raise Exception("Bad hinge point {}".format(hinge))
    lines = ax.plot(np.array([x1, x2, x3, x1]), np.array([y1, y2, y3, y1])) #, linewidth=2.0)
    return lines

#plt.ion() # Interactively display updates as they're plot()ted
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)

"""
#  start vertex          vertex plot order
=========================================
1  start at L            L -> T -> R # Doesn't fit with remaining pattern, so
                                     # plotting it outside the loop for now...
2  start at R of 1       T -> R -> L
3  start at L of 2       R -> L -> T
4  start at T of 3       L -> T -> R
5  start at R of 4       T -> R -> L
6  start at L of 5       R -> L -> T
"""

# Special case of first triangle
sidelength = 1.0
#prev_sidelengths = [1.0]
height = np.sqrt([ sidelength**2.0 - (sidelength / 2.0) ])[0]
# Plot in order: L -> T -> R
startx = starty = 0
x1 = startx + sidelength # right
y1 = starty # right
x2 = startx + (sidelength / 2.0) # top
y2 = starty - height # top
x3 = startx # left
y3 = starty # left
#plt.plot([x1], [y1], 'ro')
lastlines = ax.plot(np.array([x1, x2, x3, x1]), np.array([y1, y2, y3, y1])) #, linewidth=2.0)

# Plot remaining triangles in a loop
hinge = "right"
for i in range(0, 9):
    if i % 2 == 0:
        invert = False
    else:
        invert = True
    lastlines = plot_equilateral_triangle(
            sidelength,
            index=i,
            lastlines=lastlines,
            hinge=hinge,
            invert=invert)
    #prev_sidelengths.append(sidelength)
    #sidelength = sidelength + prev_sidelengths[-2]
    sidelength = sidelength * golden
    # Toggle hinge from right -> left -> top -> ...
    if hinge == "right":
        hinge = "left"
    elif hinge == "left":
        hinge = "top"
    elif hinge == "top":
        hinge = "right"

# Don't let aspect ratio get squashed
plt.axes().set_aspect('equal', 'datalim')
plt.show()
#while True:
#    plt.pause(0.05)
