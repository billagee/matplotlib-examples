#!/usr/bin/env python

# See http://matplotlib.org/examples/mplot3d/wire3d_demo.html

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.axes3d import Axes3D

fig = plt.figure()

# Dataset size
size = 40 # 80 # 400

ax = fig.add_subplot(111, projection='3d')

# Create 2d array for X
x_row = np.arange(size)       # array([0, 1, 2, 3])
X = np.tile(x_row, (size, 1)) # repeat x_row 4 times
Y = np.rot90(X, 3)            # Y is X rotated 270 deg counter-clockwise
Z = np.zeros((size, size))    # 4x4 2d array of 1s

# Step by 10 through all x values starting at 1, setting z value for each
for i in range(1, size, 10):
    for j in range(9, 20):
        Z[j][i] = 1
    for j in range(9, 15):
        Z[j][i] = 1
    for j in range(9, 7):
        Z[j][i] = 1

print(X) ; print(Y) ; print(Z)

#ax.set_zlim3d(0, .1)

#ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
#ax.plot_surface(X, Y, Z, rstride=10, cstride=10, cmap='hot')

# Ooh, looks nice at size=40
#ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
#                           linewidth=1, antialiased=False)
#ax.plot_surface(X, Y, Z, rstride=10, cstride=10, color="white", shade=False, edgecolor="blue")
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=.1, color="white", shade=False, edgecolor="blue")

# Looks nice at size 80
#ax.plot_surface(X, Y, Z,
#        rstride=10, cstride=10, cmap=cm.coolwarm,
#        linewidth=.1, antialiased=True)

# Plain old red and blue
#ax.plot_surface(X, Y, Z,
#        rstride=1, cstride=1, cmap=cm.coolwarm,
#        linewidth=1, antialiased=True)

#ax.plot_wireframe(X, Y, Z,
#        rstride=1, cstride=1,
#        cmap=cm.coolwarm,
#        linewidth=1, antialiased=True)

# X lines only
#ax.plot_wireframe(X, Y, Z,
#        rstride=0, cstride=1,
#        cmap=cm.coolwarm,
#        linewidth=.1, antialiased=True)

# For size 80
ax.auto_scale_xyz([0, size], [0, size], [0, 12])
# For size 400
#ax.auto_scale_xyz([0, size], [0, size], [0, 8])

plt.title('Foo')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
