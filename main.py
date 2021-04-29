from Car import Car
from Track import Track
import matplotlib.pyplot as plt
import numpy as np


test = Car(1,0,100,0,10,1.5,0.1,100)

#create a funky looking set of points
xp = [10*np.cos(np.radians(i*3.1)) for i in range(0,90)]
yp = [j%45*np.sin(np.radians(j*3.9)) for j in range(0,90)]

my_points = [list(x) for x in zip(xp, yp)]

#make sure the last point = the first point. 
my_points[len(my_points) - 1] = my_points[0]

track = Track(my_points,0.2) #[[0,0],[0,1],[1,1],[1,0],[0,0]] 

track.build_track()

xs, ys = zip(*track.midpoints) #create lists of x and y values for plotting
x1, y1 = zip(*track.interior)
x2, y2 = zip(*track.exterior)

plt.plot(xs,ys)
plt.plot(x1,y1)#c='r')
plt.plot(x2,y2)
plt.show()  