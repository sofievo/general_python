import numpy as np
import cmath
import matplotlib.pyplot as plt


## Spørsmål 1
z1 = complex(2,5)
z2 = complex(2,1)
z3 = complex(1,-1)
z4 = complex(1,-2)
# regner ut z
z = (z1*z2*z3)/z4
# regner ut magnituden (evt funker abs(z))
mag = np.sqrt(z.real**2 + z.imag**2)
mag = np.round(mag,2)
print('z = '+ str(z) + '\n|z| = ' + str(mag))


## Spørsmål 3
dt = 0.1 # steg
t = np.arange(0, 10 + dt, dt) # tidsakse
vec0 = np.array([1,0,0]) # initialverdi

# definerer funksjon f av variablene x, y, z
fx = lambda x, y, z: 1.5*x -0.1*y -2.0*z
fy = lambda x, y, z: 1.4*x +0.1*y -2.0*z
fz = lambda x, z: 3.0*x - 3.5*z
# funksjon func med input 3d np.array = (x, y, z)
def func(arr):
    x = arr[0]
    y = arr[1]
    z = arr[2]
    return np.array([fx(x,y,z), fy(x,y,z), fz(x,z)])


# 3D Eulers medode
def Euler(f, s0, dt):
    s = np.zeros((len(t),3))
    s[0] = vec0
    for i in range(0, len(t) - 1):
        s[i + 1] = s[i] + dt*f(s[i])
    return s

# Løsning
sol = Euler(func, vec0, dt)

# Plot
plt.plot(t, sol[:,0], label = 'x')
plt.plot(t, sol[:,1], label = 'y')
plt.plot(t, sol[:,2], label = 'z')
plt.grid()
plt.legend()
plt.show()


