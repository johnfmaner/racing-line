from Car import Car
from Track import Track
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    test = Car(1,0,100,0,10,1.5,0.1,100)

    #create a funky looking set of points
    xp = [30*np.cos(np.radians(i*3.1)) for i in range(0,90)]
    yp = [j%45*np.sin(np.radians(j*3.9)) for j in range(0,90)]

    my_points = [list(x) for x in zip(xp, yp)]

    #make sure the last point = the first point. 
    my_points[len(my_points) - 1] = my_points[0]

    track = Track(my_points,0.2) #[[0,0],[0,1],[1,1],[1,0],[0,0]] 

    track.build_track()
    fig = track.track_figure()
    plt.show()