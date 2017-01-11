#!/usr/bin/env python3.5

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import golden

def plot_equilateral_triangle(
        sidelength, index=0, lastlines=None,
        hinge="right", invertx=False, inverty=False):
    #import pdb ; pdb.set_trace()
    # Find equilateral triangle height by halving it and finding the long side # of the resulting right triangle.
    # See Google pythagorean calc search:
    #   a = sqrt(c^2 - b^2)
    #   pythagorean theorem calc: find a, b=n/a, c=n/a
    #   https://www.google.com/search?q=pythagorean+theorem+calc%3A+find+a%2C+b%3Dn%2Fa%2C+c%3Dn%2Fa
    height = np.sqrt([ sidelength**2 - (sidelength / 2.0) ])[0]

    # (x1,y1) is the triangle's left vertex, (x2,y2) the right, (x3,y3) the top
    startx = starty = None
    """
    #  start vertex          vertex plot order
    =========================================
    1  start at L            L -> T -> R # Doesn't fit with remaining pattern
    2  start at R of 1       T -> R -> L
    3  start at L of 2       R -> L -> T
    4  start at T of 3       L -> T -> R
    5  start at R of 4       T -> R -> L
    6  start at L of 5       R -> L -> T
    """
    print("Plotting triangle {} starting at {} of old one".format(index, hinge))
    if hinge == "left":
        startx = lastlines[0].get_xdata()[1]
        starty = lastlines[0].get_ydata()[1]
    elif hinge == "right":
        startx = lastlines[0].get_xdata()[1]
        starty = lastlines[0].get_ydata()[1]
    elif hinge == "top":
        startx = lastlines[0].get_xdata()[2]
        starty = lastlines[0].get_ydata()[2]
    else:
        raise Exception("Bad hinge point {}".format(hinge))
    # Plot dot at start point
    #plt.plot([startx], [starty], 'ro')
    x1 = startx
    y1 = starty
    if invertx:
        x2 = startx + sidelength
        x3 = startx + (sidelength / 2.0)
    elif hinge == "top":
        x2 = startx + sidelength
        x3 = startx + (sidelength / 2.0)
    else:
        x2 = startx - sidelength
        x3 = startx - (sidelength / 2.0)
    y2 = starty
    if inverty:
        y3 = starty - height
    else:
        y3 = starty + height
    lines = ax.plot(np.array([x1, x2, x3, x1]), np.array([y1, y2, y3, y1]), linewidth=2.0)
    return lines

#plt.ion() # Interactively display updates as they're plot()ted
fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid(True)

# Special case of first triangle that starts at (0,0)
# Points plotted in order of L -> T -> R
sidelength = 1
prev_sidelengths = [1]
height = np.sqrt([ sidelength**2 - (sidelength / 2.0) ])[0]
startx = starty = 0
x1 = startx
y1 = starty
x3 = startx + sidelength # right vertex, but plotted last
y3 = starty
x2 = startx + (sidelength / 2.0) # top
y2 = starty - height
plt.plot([x2], [y2], 'ro')
lastlines = ax.plot(np.array([x1, x2, x3, x1]), np.array([y1, y2, y3, y1]))

# Plot remaining triangles in a loop
hinge = "right"
for i in range(0, 4):
    if i % 2 == 0:
        invertx = False
        inverty = False
    else:
        invertx = True
        inverty = True
    lastlines = plot_equilateral_triangle(
            sidelength,
            index=i,
            lastlines=lastlines,
            hinge=hinge,
            invertx=invertx, inverty=inverty)
    prev_sidelengths.append(sidelength)
    sidelength = sidelength + prev_sidelengths[-2]
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
