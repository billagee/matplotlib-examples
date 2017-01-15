#!/usr/bin/env python3.5

import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=True)
ax.grid(True)

# https://rechneronline.de/pi/equilateral-triangle.php
# To solve for a triangle's incircle radius when side length (a) is known:
# ri = √3 / 6 * a

# So to get the side length from the incircle radius:
# a = ri / (√3 / 6)
# e.g., with a radius of 2,
# a = 2 / (√3 / 6)
prev_radii = []
startx = starty = 0
start_radius = 1
start_sidelen = start_radius / (math.sqrt(3) / 6)
#print("Plotting x{} y{} r{}".format(startx, starty, start_radius))
print("Plotting triangle with:")
print("  x: {}\ty: {}\tr: {}\t sidelen: {}".format(
    startx, starty, start_radius, start_sidelen))
ax.add_patch(
    patches.RegularPolygon(
        (startx, starty), 3, # (x,y) tuple and number of vertices
        radius=start_radius,
        #hatch='|',
        orientation=math.pi,  # orientation in radians
    )
)
plt.plot([startx], [starty], 'ro') # plot dot at center of triangle

# Second triangle
#start_sidelen = start_radius / (math.sqrt(3) / 6)
#newx = startx - ((start_sidelen / 2) / 2)
#newy = starty + start_radius / 2
prev_radii.append(start_radius)
next_radius = start_radius # Special case for 2nd triangle
next_sidelen = next_radius / (math.sqrt(3) / 6)
next_x = startx - ((start_sidelen / 2) / 2)
next_y = starty - start_radius / 2
plt.plot([startx], [starty], 'ro')
#print("Plotting x{} y{} r{}".format(newx, newy, start_radius))
print("Plotting triangle with:")
print("  x: {}\ty: {}\tr: {}\t sidelen: {}".format(
    next_x, next_y, next_radius, next_sidelen))
p = ax.add_patch(
    patches.RegularPolygon( (next_x, next_y), 3, radius=next_radius, )
)
plt.plot([next_x], [next_y], 'ro')

# Third triangle
#prev_radii = [ start_radius ]
prev_radii.append(start_radius)
next_radius = start_radius + prev_radii[-2]
next_sidelen = next_radius / (math.sqrt(3) / 6)
next_x = startx
next_y = starty - start_radius * 2
print("Plotting triangle with:")
print("  x: {}\ty: {}\tr: {}\t sidelen: {}".format(
    next_x, next_y, next_radius, next_sidelen))
ax.add_patch(
    patches.RegularPolygon(
        (next_x, next_y), 3,
        radius=next_radius,
        orientation=math.pi,  # orientation in radians
    )
)
plt.plot([next_x], [next_y], 'ro')

# Fourth triangle
prev_radii.append(next_radius)
import pdb ; pdb.set_trace()
next_radius = prev_radii[-1] + prev_radii[-2]
next_sidelen = next_radius / (math.sqrt(3) / 6)
next_x = next_sidelen / 4 # 2.5980762
next_y = -2.5
#next_x = startx
#next_y = starty - start_radius * 2
print("Plotting triangle with:")
print("  x: {}\ty: {}\tr: {}\t sidelen: {}".format(
    next_x, next_y, next_radius, next_sidelen))
ax.add_patch(
    patches.RegularPolygon(
        (next_x, next_y), 3,
        radius=next_radius,
    )
)
plt.plot([next_x], [next_y], 'ro')
#(2.598, -2.5), 3,
#(2.5980762119999996, -2.5), 3,

# Fifth triangle
# prev sidelen / 2 = 3.4641015
# next_sidelen / 2 = 8.660254037844388
prev_radii.append(next_radius)
next_x = next_sidelen / 2
next_y = 1
next_radius = prev_radii[-1] + prev_radii[-2]
next_sidelen = next_radius / (math.sqrt(3) / 6)
#next_x = (3.4641015 / 2) / 2 + 8.660254037844388 / 2
print("Plotting triangle with:")
print("  x: {}\ty: {}\tr: {}\t sidelen: {}".format(
    next_x, next_y, next_radius, next_sidelen))
ax.add_patch(
    patches.RegularPolygon(
        (next_x, next_y), 3,
        radius=next_radius,
        orientation=math.pi,  # orientation in radians
    )
)
plt.plot([next_x], [next_y], 'ro')

#fig.savefig('reg-polygon1a.png', dpi=90, bbox_inches='tight')

#set the limit of the axes to -3,3 both on x and y
#ax.set_xlim(-2,2)
#ax.set_ylim(-2,2)
#plt.axis('image') #auto')
#plt.axis('auto')
plt.axis('scaled')
plt.show()

