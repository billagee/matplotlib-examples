#!/usr/bin/env python3.5

import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D

x = [[1., 2., 3., 4.],
     [1., 2., 3., 4.],
     [1., 2., 3., 4.],
     [1., 2., 3., 4.]]
y = [[1., 1., 1., 1.],
     [1., 1., 1., 1.],
     [1., 1., 1., 1.],
     [1., 1., 1., 1.]]
z = [[1,  1,  1,  1],
     [2,  2,  2,  2],
     [3,  3,  3,  3],
     [4,  4,  4,  4]]

fig = matplotlib.pyplot.figure()
ax  = fig.add_subplot(111, projection = '3d')

ax.plot_wireframe(x, y, z, rstride=1, cstride=1, color='b')

matplotlib.pyplot.show()
