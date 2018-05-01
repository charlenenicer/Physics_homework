import math
import numpy
import matplotlib.pyplot

h = 0.00001
g = 9.8
rho = 1.23
radius = 0.0365
cd = 0.5
a = 3.14*radius**2
m = 0.143
num_steps = 448999;

acceleration = numpy.array([0., -g])
initial_speed = 60
angle_rad = math.pi/180. * 30

def accfunc(x,v):
    v_mag = ((v[0]**2)+(v[1]**2))**(0.5)
    ax = -0.5*cd*a/m*rho*v[0]*v_mag
    ay = -g -0.5*cd*a/m*rho*v[1]*v_mag
   
    return numpy.array([ax, ay])

    
    

def trajectory():


	x = numpy.zeros([num_steps + 1, 2])
	v = numpy.zeros([num_steps + 1, 2])

	x[0, 0] = 0.
	x[0, 1] = 0.
	v[0, 0] = initial_speed * math.cos(angle_rad)
	v[0, 1] = initial_speed * math.sin(angle_rad)
	for step in range(num_steps):
          x[step + 1] = x[step] + h*(v[step])
          v[step + 1] = v[step] + h*accfunc(x[step], v[step])
          
                  
      
        
		

	return x, v

x, v = trajectory()
print(x[num_steps])
#land = numpy.where(v[1]<0)
#solution = v[0:,]
#answer = solution[land]
#print(answer)

#print("range:", x[(22500)])
#print("velo:", v[(3060)])
print("terminal velocity:", v[num_steps])

t = 2*initial_speed * math.sin(angle_rad)/g
print(t)
print(num_steps*h)
print(v[num_steps])
matplotlib.pyplot.plot(x[:, 0], x[:,1])
matplotlib.pyplot.xlabel('{} [{}]'.format("range", "m"))
matplotlib.pyplot.ylabel('{} [{}]'.format("height","m"))
matplotlib.pyplot.title(r'Trajectory of a projectile motion with drag')
