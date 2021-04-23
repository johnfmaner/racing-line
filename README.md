# racing-line

## Problem Statement: 
Given a course with a definite inside and outside boundary, and a car with finite grip (coefficient of friction) and performance (rate of acceleration and deceleration), find the fastest path around the track while staying within the course. 

## Newtownian physics: 

### Centripetal acceleration: 
The centrifugal acceleration is given to be: F = m v^2 / r. 

### Friction force 
The friction force is given to be: F = mu N = mu m g (assume the surface is flat at all times, and that gravity only every points directly down). 

### Equilibrium condition
A body is said to be in equilibirum when the sum of all forces is equal to 0. Given our car, which experiences a friction force and centripetal acceleration while turning, the following must be true to prevent the car from sliding: 

F_friction > F_centripetal.
m v^2 / r  >  mu m g  =>  v_max = (mu g r)^1/2 

Our goal is to continously find an r along which our car can travel such that the car remains in the track boundaries at all times while minimizing the lap time. 

### Changing speed
Consider the case in which the car is approaching a sharp corner after accelerating for a very long time (v >> v_max). It is obvious that the corresponding radius will exceed the track limits. It becomes necessary for the car to change speed before entering a corner. Likewise, if the car starts from rest, it will never reach the corner in the first place unless we allow the car to accelerate. Additionally, the car may need to accelerate to avoid travelling along an arc which will exceed the track limits. 

For simplicity, a coefficient of performance, "cop", will be chosen how quickly the car can brake and accelerate. The relation is chosen to be linear such that: 

|dv / dt| = cop

## Future considerations: 

### Downforce
Downforce is an additional force which results from the collisions of air molecules with the bodywork of a car, pushing the car downwards. It is reasonable to see that the faster the car travels, the harder the air molecules collide with the car, and the harder the car is pressed into the ground. We will model this by making the mass a function of velocity: 

m(v) = m_0 (1 + v^2 / C_down), 

where C_down is a sufficiently large coefficent of downforce to allow the effective mass of the car to increase reasonably quickly at higher speeds. Notice in the limit v -> 0 that m(v->0) = m_0, the original mass. 

### Drag 
In future, we may consider a drag force which is proportional to the square of the velocity. For our purposes, this force will look like: 

F_drag = C_drag  v^2, where C_drag is a constant we would aim to minimize as race car designers. 

### Additional considerations 
It is worth noting that our C_down and C_drag coefficients should likely be coupled. That is, the more fancy aerodynamics I add to my car, the more bits of bodywork there are to disturb the pristine air from flowing over the bodywork and miniming drag. This relation may be explored further once the aforementioned ideas are implemented. 

### New equilibirum condition 
Now considering Downforce, our new equilibirum condition looks like: 

Lateral forces: m(v) v^2 /r > mu m g => m_0 (1+v^2 / C_down) v^2 / r > mu m g => v_max = ((C_down * (4 mu g r + C_down)^1/2 - C_down)^1/2 / (2)^1/2. 

## Defining a track

### Track limits
The track must have a definite inside and outside. For ease of calculation, a set of points will be defined known as the midpoint. From each midpoint, two points will be generated at a desired distance from the midpoint to create an "inside" and an "outside". 

TBD. 

## Algorithm 

### Calculating acceleration 
Runge Kutta? Something more simple? 

### Circle fitting 
We must fit circles of radius r which allow the car to maximize velocity while remaining within the track limits. How will the track limits play into this algorithm? 
