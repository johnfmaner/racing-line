# racing-line

## Problem Statement: 
Given a course with a definite inside and outside boundary, and a car with finite grip (coefficient of friction) and performance (rate of acceleration and deceleration), find the fastest path around the track while staying within the course. 

## Newtownian physics: 

### Centripetal acceleration: 
The centrifugal acceleration is given to be: 

F = m v^2 / r

Where v is the velocity tangential to the circle of radius r. 

### Friction force 
We will assume the surface the car travels along is flat at all times, and the the gravity force only ever points directly down. The friction force is given to be: 

F = mu N = mu m g 

### Equilibrium condition
A body is said to be in equilibirum when the sum of all external forces is equal to 0. Our car, which experiences a friction force and centripetal force while turning, should remain in equilibrium by not exceeding the max speed allowed by the performance of the tires (coefficient of friction). That is, 

F_friction > F_centripetal

m v^2 / r  >  mu m g  

=>  v_max = (mu g r)^1/2 

Our goal, in the simplest terms, is to find a set of circles along which our car will travel such that the car remains in the track boundaries at all times while minimizing the lap time. 

### Changing speed
Consider the case in which the car is approaching a sharp corner which has a corresponding v_max much less than the current velocity. It is obvious that the corresponding radius will exceed the track limits. It becomes necessary for the car to change speed before entering a corner. Likewise, if the car starts from rest, it will never reach the corner in the first place unless we allow the car to accelerate. Additionally, the car may need to accelerate to avoid travelling along an arc which will exceed the track limits. 

For simplicity, a coefficient of performance, "cop", will be chosen how quickly the car can brake and accelerate. The relation is chosen to be linear such that: 

|dv / dt| = cop

## Future considerations: 

### Downforce
Downforce is an additional force which results from the collisions of air molecules with the bodywork of a car, pushing the car downwards. It is reasonable to see that the faster the car travels, the harder the air molecules collide with the car, and the harder the car is pressed into the ground. We will model this by making the mass a function of velocity: 

m(v) = m_0 (1 + v^2 / C_down), 

where C_down is a sufficiently large coefficent of downforce to allow the effective mass of the car to increase reasonably quickly at higher speeds. Notice in the limit v -> 0 that m(v->0) = m_0, the original mass. 

### Drag 
In future, we may consider a drag force which is proportional to the square of the velocity. For our purposes, this force will look like: 

F_drag = -C_drag  v^2

Where C_drag is a property of our car. This will prevent the car from accelerating unreasonably quickly, and subsequently will lead to different racing lines. 

### Additional considerations 
It is worth noting that our C_down and C_drag coefficients should likely be coupled. That is, as I add more fancy bodywork to generate downforce, more bodywork can disturb the pristine air from flowing over the bodywork, generating drag. This relation may be explored further once the aforementioned ideas are implemented. 

### New equilibirum condition 
Now considering Downforce, our new equilibirum condition looks like: 

Lateral forces: 

m(v) v^2 /r > mu m g 

=> m_0 (1+v^2 / C_down) v^2 / r > mu m g 

=> v_max = ((C_down * (4 mu g r + C_down)^1/2 - C_down)^1/2 / (2)^1/2. 

## Defining a track

### Track limits
The track must have a definite inside and outside. For ease of calculation, a set of points will be defined known as the midpoints. The inside and outside will be determined use a scale factor, called the width, such that 0 < width < 1. 

### Calculation 
The midpoints are provided as a list of 2d vectors. To calculate the inner boundary each midpoint vector, m_i, is multiplied by a scaling matrix, where the scaling factor is determined by the width: 
```
m_inner_i = m_i [1-width         0  ]
                [    0       1-width]
```

Correspondingly, the outer boundary is calculated by: 

```
m_outer_i = m_i [1+width         0  ]
                [    0       1+width]
```

It is now clear that the width must be between 0 and 1, else the inner boundary would reflect across the line y = x and actually expand.  

## Algorithm 

### Calculating acceleration 
Our goal is to travel at the highest speed for the longest time to minimize our lap time. The car should try to accelerate at each time step in order to travel at a higher speed, within the limits of the performance of the tires (coeffient of friction). 

### Circle fitting 
We must fit circles of radius r which allow the car to maximize velocity while remaining within the track limits. How will the track limits play into this algorithm? 
