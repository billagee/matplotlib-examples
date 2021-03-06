#!/usr/bin/env python3.5

import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
from scipy.constants import golden

def plot_equilateral_triangle(
        sidelength, index=0, lastpatch=None,
        hinge="right", invert=False, fillcolor=None):
    # Find equilateral triangle height:
    height = math.sqrt(3.0) * (sidelength / 2.0)

    print("Plotting triangle {} starting at {} of old one".format(index, hinge))
    startx = starty = None
    # Start points will always be third vertex plotted in the prev triangle
    startx = lastpatch.xy[2][0]
    starty = lastpatch.xy[2][1]
    # Plot dot at start point
    #plt.plot([startx], [starty], 'ro')
    if hinge == "left":
        # Triangles started from left of prev get their vertices
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
        # Triangles started from right of prev get their vertices
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
        # Triangles started from top of prev get their vertices
        # plotted in this order:
        # L -> T -> R
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

    patch = ax.add_patch(
            Polygon([[x1, y1], [x2, y2], [x3, y3]],
                closed=True, fill=True, facecolor=fillcolor, label="s"))
    # Add text to center of polygon
    cx = (x1 + x2 + x3) /  3
    cy = (y1 + y2 + y3) /  3
    ax.annotate(sidelength, (cx, cy),
            color='w', weight='bold', fontsize=10,
            ha='center', va='center')
    return patch

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
prev_sidelengths = [1.0]
height = math.sqrt(3.0) * (sidelength / 2.0)
# Plot in order: L -> T -> R
startx = starty = 1
x1 = startx + sidelength # right
y1 = starty # right
x2 = startx + (sidelength / 2.0) # top
y2 = starty - height # top
x3 = startx # left
y3 = starty # left
#plt.plot([x1], [y1], 'ro')
lastpatch = ax.add_patch(Polygon([[x1, y1], [x2, y2], [x3, y3],], closed=True,
                          fill=True, facecolor="#666666"))

# Plot remaining triangles in a loop
hinge = "right"
for i in range(0, 10):
    if i % 2 == 0:
        invert = False
    else:
        invert = True
    lastpatch = plot_equilateral_triangle(
            sidelength,
            index=i,
            lastpatch=lastpatch,
            hinge=hinge,
            invert=invert,
            fillcolor='#666666')

    prev_sidelengths.append(sidelength)
    sidelength = sidelength + prev_sidelengths[-2]
    #sidelength = sidelength * golden

    # Toggle hinge from right -> left -> top -> ...
    if hinge == "right":
        hinge = "left"
    elif hinge == "left":
        hinge = "top"
    elif hinge == "top":
        hinge = "right"

# First triangle of second batch
sidelength = 1.0
prev_sidelengths = [1.0]
height = math.sqrt(3.0) * (sidelength / 2.0)
# Plot in order: L -> T -> R
startx = 1.5
#startx = 3.5
starty = 1 - height
x1 = startx # left
y1 = starty # left
x2 = startx + (sidelength / 2.0) # top
y2 = starty + height # top
x3 = startx + sidelength # right
y3 = starty # right
#plt.plot([x1], [y1], 'ro')
lastpatch = ax.add_patch(Polygon([[x1, y1], [x2, y2], [x3, y3],], closed=True,
                          fill=True, color="#35206f"))

# Second batch
hinge = "right"
for i in range(0, 10):
    if i % 2 == 0:
        invert = True
    else:
        invert = False
    lastpatch = plot_equilateral_triangle(
            sidelength,
            index=i,
            lastpatch=lastpatch,
            hinge=hinge,
            invert=invert,
            fillcolor='#35206f')

    prev_sidelengths.append(sidelength)
    sidelength = sidelength + prev_sidelengths[-2]
    #sidelength = sidelength * golden

    # Toggle hinge from right -> left -> top -> ...
    if hinge == "right":
        hinge = "left"
    elif hinge == "left":
        hinge = "top"
    elif hinge == "top":
        hinge = "right"

# Don't let aspect ratio get squashed
plt.axes().set_aspect('equal', 'datalim')
ax.set_xlim((-30, 30))
ax.set_ylim((-30, 30))
plt.show()
#while True:
#    plt.pause(0.05)
