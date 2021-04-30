import numpy as np 
import matplotlib.pyplot as plt

class Track(object):
    def __init__(self,midpoints:list,width:float):
        mlen = len(midpoints) - 1
        
        if type(midpoints) is not list: 
            raise TypeError("Midpoints must be a list.")

        if midpoints[0][0] != midpoints[mlen][0] and midpoints[0][1] != midpoints[mlen][1]:
            raise ValueError("First point must equal the last point.")

        if mlen < 3:
            raise ValueError("At least 3 points must be defined.")

        self.midpoints = np.array(midpoints)

        assert 0 < width < 1, "Width must be between 0 and 1."
        self.width = width

    def boundary_length(self,points): 
        """calculate the cartesian length of a list of points"""
        mlen = len(points)
        total_dist = 0

        for i in range(0,mlen):
            dx = points[i%mlen][0] - points[(i+1)%mlen][0]
            dy = points[i%mlen][1] - points[(i+1)%mlen][1]

            total_dist += pow(dx*dx + dy*dy, 0.5)

        return total_dist 

    def direction_vector(self,p1,p2):
        """calculate the vector between two points"""
        # assert (len(p1) = len(p2) and len(p2) = 2), "Input vectors must be two dimensional"

        return np.array([p2[0] - p1[0],p2[1] - p2[0]])  

    def perp_vector_cw(self, vec):
        """returns the input vector rotated 90 degrees cw""" 
        cw = np.array([vec[1],-vec[0]])
        return cw

    def perp_vector_ccw(self,vec):
        """returns the input vector rotated 90 degrees ccw""" 
        ccw = np.array([-vec[1],vec[0]])
        return ccw

    def reflect_vector(self,vec):
        """reflect an input vector"""
        
        return np.matmul(vec, np.array([[1,0],[0,1]])) #rotation matrix for theta = 180 deg

    def normalize(self,vec):
        """normalize an input vector"""
        return vec / np.linalg.norm(vec)

    def centroid(self, points):
        """find the centroid given a list of points"""
        x = [i[0] for i in points[0:len(points)-1]] #correct for the first point being duplicated to make
        y = [i[1] for i in points[0:len(points)-1]] #a closed shape. this probably needs to be refactored. 

        x_center = sum(x)/len(x)
        y_center = sum(y)/len(y)

        return np.array([x_center,y_center])

    def build_track(self): 
        """
        build the track boundaries based on the midpoints 
        boundaries are based on affine scale transformation 
        Access the boundaries with 
        """ 
        #note -- this will only work with nice looking convex shapes. 

        lim1 = []
        lim2 = []

        #calculate the scaling matricies 
        s1 = np.array([[1-self.width,0],[0,1-self.width]])
        s2 = np.array([[1+self.width,0],[0,1+self.width]])

        # multiply the ith midpoint position vector by the scaling matrix. 
        lim1 = [np.matmul(i, s1) for i in self.midpoints]
        lim2 = [np.matmul(j, s2) for j in self.midpoints]

        #calculate centroids 
        c0,c1,c2 = self.centroid(self.midpoints),self.centroid(lim1),self.centroid(lim2) 

        #translate the scaled points to make c0 = c1 = c2
        lim1 = [i + c0 - c1 for i in lim1]
        lim2 = [j + c0 - c2 for j in lim2]

        self.interior = lim1
        self.exterior = lim2  

    def track_figure(self):
        """create a figure which can be plotted with plt.show()"""

        #this is still not as clean as I would like -- this should be a 
        #one-liner to plot the track, but returning the figure may be the
        #better idea in the long run so I can add the racing line to the
        #plot figure. For now, this is ok. 
        
        xm, ym = zip(*self.midpoints) #create lists of x and y values for plotting
        xi, yi = zip(*self.interior)
        xo, yo = zip(*self.exterior)

        f, ax = plt.subplots()
        ax.plot(xm,ym)
        ax.plot(xi,yi)#c='r')
        ax.plot(xo,yo)

        return ax