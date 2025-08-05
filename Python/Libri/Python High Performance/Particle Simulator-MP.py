#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


# ![image.png](attachment:d313c580-62b2-4cdf-8324-9a98a98424b8.png)

# In[44]:


class Particle:
    
    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


# In[1]:


class ParticleSimulator:

    def __init__(self, particle):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.001
        nsteps = int(dt/timestep)

        for i in np.arange(nsteps):
            
            for p in self.particles:
                
                ipotenusa = (p.x**2 + p.y**2)**0.5
                cos_v =  p.y/ipotenusa
                sin_v = -p.x/ipotenusa

                d_x = timestep*p.ang_vel*cos_v
                d_y = timestep*p.ang_vel*sin_v

                p.x += d_x
                p.y += d_y


# In[46]:


particles = [Particle(0.3, 0.5, 1), Particle(0.0, -0.5, -1), Particle(-0.1, -0.4, 3)] 
simulator = ParticleSimulator(particles)


# In[43]:


X = [p.x for p in simulator.particles] 
Y = [p.y for p in simulator.particles]

fig = plt.figure()
ax = plt.subplot()
line, = ax.plot(X, Y, 'ro')

# Axis limits 
plt.xlim(-1, 1) 
plt.ylim(-1, 1) 

def update(frame):
    # for each frame, update the data stored on each artist.
    simulator.evolve(0.01)
    X = [p.x for p in simulator.particles] 
    Y = [p.y for p in simulator.particles]
 
    # update the line plot:
    line.set_xdata(X)
    line.set_ydata(Y)
    return line


anim = animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=10)
plt.show()

