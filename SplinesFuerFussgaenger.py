#!/usr/bin/env python3
import numpy as np
import matplotlib
import matplotlib.pylab as pylab

class Spline:
    def __init__(self, x,y):
        if len(x) is not len(y):
            print("ungültige Eingabe!")
            exit()
        self._x = np.array(x); self._y = np.array(y)
        self._N = len(x)
        self._S = self._N - 1
        self._U = self._S - 1
        self._C = 4 * self._S

        A, b = self.sys(self._x, self._y)
        print(A)
        self._coef = np.linalg.solve(A,b)

    def S(self, i, x):
        v = np.zeros( (self._C,))
        v[(i*4):((i+1)*4)] = [1, x, x**2, x**3]
        return v

    def dS(self, i, x):
        v = np.zeros( (self._C,))
        v[(i*4):((i+1)*4)] = [0, 1, 2*x, 3*x**2]
        return v

    def ddS(self, i, x):
        v = np.zeros( (self._C,))
        v[(i*4):((i+1)*4)] = [0, 0, 2, 6*x]
        return v

    def sys(self, x, y):
        A = np.zeros( (self._C, self._C) )
        b = np.zeros( (self._C,) )
        r = 0
        # s''_1(x_0) = 0
        A[r,:] = self.ddS(0, x[0]); b[r] = 0; r += 1
        # Anfangswerte der Splines s_i(x_{i-1}) = y_{i-1}
        for s in range(self._S):
            A[r,:] = self.S(s, x[s]); b[r] = y[s]; r += 1
        A[r,:] = self.S(self._S-1, x[self._N-1]); b[r] = y[self._N-1]; r += 1
        # Alle Übergänge
        for u in range(self._U):
            # s_i(x_i) = s_{i+1}(x_i)
            A[r,:] =   self.S(u,x[u+1]) -   self.S(u+1,x[u+1]); b[r] = 0; r += 1
            # s'_i(x_i) = s'_{i+1}(x_i)
            A[r,:] =  self.dS(u,x[u+1]) -  self.dS(u+1,x[u+1]); b[r] = 0; r += 1
            # s''_i(x_i) = s''_{i+1}(x_i)
            A[r,:] = self.ddS(u,x[u+1]) - self.ddS(u+1,x[u+1]); b[r] = 0; r += 1
        # s''_n(x_n)=0
        A[r,:] = self.ddS(self._S-1, x[self._N-1]); b[r] = 0; r += 1
        return A, b

    def plot(self, col="b:", N=20):
        pylab.plot(self._x, self._y, "k.")
        for i in range(self._S):
            x = np.linspace(self._x[i], self._x[i+1], N)
            A = np.empty((N, 4))
            A[:,0] = 1
            A[:,1] = x
            A[:,2] = x**2
            A[:,3] = x**3
            pylab.plot(x, np.dot(A, self._coef[(4*i):((i+1)*4)]), col)

    def coef(self):
        return self._coef

spl = Spline([1, 3, 5, 6, 8, 9, 12, 16, 19], [0, 3, 1, 7, 8, 4, 12, 1, 50])
spl.plot()
#pylab.xlim(-1,7)
pylab.ylabel("y")
pylab.xlabel("x")
pylab.show()
print(spl.coef())
