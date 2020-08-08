from math import pi, sin
from numpy import *
from matplotlib import pylab

x = linspace(0,2*pi,100)
y = sin(x)
y2 = cos(x)
pylab.plot(x,y, "k:", label="sin(x)")
pylab.plot(x,y2, "r--", label="cos(x)")
pylab.xlabel("x")
pylab.ylabel("y")
pylab.legend()
pylab.show()

x = linspace(0, 2*pi, 100)
pylab.subplot(2,1,1)
pylab.plot(x, sin(x), label="sin(x)")
pylab.ylabel("y")
pylab.xlabel("x")
pylab.legend()
pylab.subplot(2,1,2)
pylab.plot(x, cos(x),"r", label="cos(x)")
pylab.ylabel("y")
pylab.xlabel("x")
pylab.legend()
pylab.show()

#t = linspace(0,2*pi,100)
#x = cos(t)**3
#y = sin(t)**3
#pylab.plot(x,y)
#pylab.xlim(-1,1)
#pylab.ylim(-1,1)
#pylab.savefig("test.pdf")

x = linspace(0,6*pi,1000)
y = linspace(0,6*pi,1000)
z = outer(sin(x),cos(y))
pylab.contour(x,y,z, 300)
pylab.show()