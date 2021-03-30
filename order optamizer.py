x0 = .5
y0 = 5
z0 = 22
wp0 = 'O'
origin = (x0, y0, z0, wp0) #This is the origin points above from where ever they come from in a list thing
X0 = [5.1, 2, 3, 4] #enter x part of coordinate
Y0 = [60, 20, 30, 40] #enter y part of coordinate
Z0 = [84, 55, 66, 77] #Enter Z coordinates
WPlist = [ 'B', 'C', 'A' ,'D']
points = zip(X0, Y0, Z0,WPlist) # converting values to print as list, stays in same order but not a list
points = list(points) # turns zipped thing into sortable list
ordered = [origin] #Gives an empty set, origin inside adds the origin back to the list of points so we can start at the origin
current_point = (x0, y0, z0, wp0)

while len(points) > 0:
   min_distance = float('inf')
   x0, y0, z0, wp0 = current_point
   for (x, y, z, WP) in points:
       distance = ((x - x0) ** 2 + (y - y0) ** 2 + (z - z0) ** 2) ** (1 / 2)  # compute distance

       if distance < min_distance:
           min_distance = distance
           closest = (x, y, z, WP)

   ordered.append(closest)
   points.remove(closest)
   current_point = closest
ordered.append(origin) #Appends the origin to the end of the list so the drone returns home
print(ordered) #Prints out the value for the ordered list of points to go to.

test_list = ordered
print("Original list is : " + str(test_list)) # Printing original list
res = list(zip(*test_list)) # Using zip() and * operator to perform Unzipping
print("Modified list is : " + str(res)) # Printing modified list
XXX = res[0] #These 3 lines get the X, Y, X values from the ordered system
YYY = res[1]
ZZZ = res[2]
WPP = res[3]
print(XXX) #Prints the values so you can see the X, Y, Z, Waypoints in the optimized order
print(YYY)
print(ZZZ)
print(WPP)

#3D plots the points as they are in the new order

# importing mplot3d toolkits, numpy and matplotlib
# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt
# fig = plt.figure()
# # syntax for 3-D projection
# ax = plt.axes(projection='3d') # # defining all 3 axes
# # plotting
# ax.plot3D(XXX, YYY, ZZZ, *-*)
# plt.show()

## Start working on the next section of code here.
