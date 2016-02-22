import GeePea
import numpy as np
import pylab

x = np.linspace(0,1,50)
y = np.sin(2*np.pi*x) + np.random.normal(0,0.1,x.size)

p = [1,1,0.1]

gp = GeePea.GP(x,y,p)

gp.optimise()

pylab.figure(1,(6,4))

gp.plot()

pylab.xlabel('x')
pylab.ylabel('y')