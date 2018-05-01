import math
import numpy
import matplotlib.pyplot

h = 0.0001
g = 9.8


acceleration = numpy.array([0., -g])
initial_speed = 60
angle_rad = math.pi/180. * 30
num_steps = 61227;


def trajectory():
	x = numpy.zeros([num_steps + 1, 2])
	v = numpy.zeros([num_steps + 1, 2])

	x[0, 0] = 0.
	x[0, 1] = 0.
	v[0, 0] = initial_speed * math.cos(angle_rad)
	v[0, 1] = initial_speed * math.sin(angle_rad)
	for step in range(num_steps):
          x[step + 1] = x[step] + h*(v[step])
          v[step + 1] = v[step] + h*acceleration
                  
      

	return x, v

x, v = trajectory()
print("range:", x[num_steps])
print("range:", x[(30613)])
#print("velo:", v[(3060)])
print("terminal velocity:", v[num_steps])

t = 2*initial_speed * math.sin(angle_rad)/g
print(t)
print(num_steps*h)
matplotlib.pyplot.plot(x[:, 0], x[:,1], label = "")
matplotlib.pyplot.xlabel('{} [{}]'.format("range", "m"))
matplotlib.pyplot.ylabel('{} [{}]'.format("height","m"))
matplotlib.pyplot.title(r'Trajectory of a projectile motion with no drag')
matplotlib.pyplot.legend 

