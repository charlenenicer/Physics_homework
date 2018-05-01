import math
import numpy
import matplotlib.pyplot

h1 = 0.0001
h2 = 0.0001
h3 = 0.00001
g = 9.8
rho = 1.23
radius = 0.0365
cd = 0.5
a = 3.14*radius**2
m = 0.143
num_steps1 = 44899;
num_steps2 = 61227;
num_steps3 = 448999;

acceleration = numpy.array([0., -g])
initial_speed = 60
angle_rad = math.pi/180. * 30

def accfunc(v):
    v_mag = ((v[0]**2)+(v[1]**2))**(0.5)
    ax = -0.5*cd*a/m*rho*v[0]*v_mag
    ay = -g -0.5*cd*a/m*rho*v[1]*v_mag
   
    return numpy.array([ax, ay])

def trajectoryCorrected():


	x1 = numpy.zeros([num_steps1 + 1, 2])
	v1 = numpy.zeros([num_steps1 + 1, 2])

	x1[0, 0] = 0.
	x1[0, 1] = 0.
	v1[0, 0] = initial_speed * math.cos(angle_rad)
	v1[0, 1] = initial_speed * math.sin(angle_rad)
	for step in range(num_steps1):
          v1_corrected = v1[step] + h1*accfunc(v1[step])
          x1[step + 1] = x1[step] + 0.5*h1*(v1[step]+ v1_corrected)
          v1[step + 1] = v1[step] + h1*accfunc((v1[step]+v1_corrected)/2)
                  
      
        
		

	return x1, v1

x1, v1 = trajectoryCorrected()


def trajectoryNoDrag():
	x2 = numpy.zeros([num_steps2 + 1, 2])
	v2 = numpy.zeros([num_steps2 + 1, 2])

	x2[0, 0] = 0.
	x2[0, 1] = 0.
	v2[0, 0] = initial_speed * math.cos(angle_rad)
	v2[0, 1] = initial_speed * math.sin(angle_rad)
	for step in range(num_steps2):
          x2[step + 1] = x2[step] + h2*(v2[step])
          v2[step + 1] = v2[step] + h2*acceleration
                  
      

	return x2, v2


x2, v2 = trajectoryNoDrag()


def trajectoryWithDrag():


	x3 = numpy.zeros([num_steps3 + 1, 2])
	v3 = numpy.zeros([num_steps3 + 1, 2])

	x3[0, 0] = 0.
	x3[0, 1] = 0.
	v3[0, 0] = initial_speed * math.cos(angle_rad)
	v3[0, 1] = initial_speed * math.sin(angle_rad)
	for step in range(num_steps3):
          x3[step + 1] = x3[step] + h3*(v3[step])
          v3[step + 1] = v3[step] + h3*accfunc(v3[step])
          
                  
      
        
		

	return x3, v3

x3, v3 = trajectoryWithDrag()




print(v1[num_steps1])
print(v3[num_steps3])
#print("range:", x[(22525)])
#print(num_steps*h)
matplotlib.pyplot.plot(x1[:, 0], x1[:,1], 'b', label = 'predictor-corrector')
matplotlib.pyplot.plot(x2[:, 0], x2[:,1], label = 'no drag')
matplotlib.pyplot.plot(x3[:, 0], x3[:,1], '--r', label = 'with drag')
matplotlib.pyplot.xlabel('{} [{}]'.format("range", "m"))
matplotlib.pyplot.ylabel('{} [{}]'.format("height","m"))
matplotlib.pyplot.title(r'Trajectory of a projectile motion')
matplotlib.pyplot.legend(loc ='best', numpoints = 1)
matplotlib.pyplot.show()

