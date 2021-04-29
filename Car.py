
class Car(object):
    """Create a Car object which contains the initial position, velocity, and car properties"""
    def __init__(self,x0:float, y0:float, vx0:float, vy0:float, mass:float, cof:float, dt:float, cop:float):
        self.x = x0
        self.y = y0

        self.vx = vx0
        self.vy = vy0
        
        assert 0 < mass, "Mass must be non-zero and positive."
        self.mass = mass

        assert 0 < cof, "Coefficient of friction must be greater than 0."
        self.cof = cof # coefficient of friction 

        assert 0 < dt, "Time step must be greater than 0."
        self.dt = dt

        assert 0 < cop, "Coefficient of performance must be greater than 0."
        self.cop = cop

    def distance(self, originX:float, originY:float): 
        """calculate the distance between the current (x,y) and an (originX,originY)."""
        xdist = originX - self.x
        ydist = originY - self.y
        return pow(xdist * xdist + ydist * ydist, 0.5) 

    def mass_update(self):
        """calculate the effective mass. Will be used for downforce in future."""
        pass 
    
    def weight(self):
        """calculate the weight force"""
        return self.mass * 9.8 #m/s^2

    def speed(self): 
        """calculate the magnitude of the velocity."""
        return pow(self.vx * self.vx + self.vy * self.vy, 0.5)

    def energy(self):
        """calculate the kinetic energy."""
        return self.mass * self.speed() * self.speed()

    def acceleration(self): 
        """update acceleration."""
        self.ax = self.cop #constant acceleration. 
        self.ay = self.cop 

    def position_step(self): 
        """update position according to current velocity"""
        self.x += self.vx * self.dt 
        self.y += self.vy * self.dt 

    def velocity_step(self):
        """update velocity according to current acceleration"""
        self.acceleration()
        self.vx +=  self.ax * self.dt 
        self.vy +=  self.ay * self.dt 