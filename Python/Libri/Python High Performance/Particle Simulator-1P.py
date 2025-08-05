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


# In[45]:


class ParticleSimulator:

    def __init__(self, particle):
        self.particle = particle

    def evolve(self, dt):
        p = self.particle
        timestep = 0.001
        nsteps = int(dt/timestep)

        for i in np.arange(nsteps):

            ipotenusa = (p.x**2 + p.y**2)**0.5
            cos_v =  p.y/ipotenusa
            sin_v = -p.x/ipotenusa

            d_x = timestep*p.ang_vel*cos_v
            d_y = timestep*p.ang_vel*sin_v

            p.x += d_x
            p.y += d_y


# In[46]:


particle = Particle(-0.3, 0.5, 2)
simulator = ParticleSimulator(particle)


# In[43]:


fig = plt.figure()
ax = plt.subplot()
line, = ax.plot(particle.x, particle.y, 'ro')

# Axis limits 
plt.xlim(-1, 1) 
plt.ylim(-1, 1) 

def update(frame):
    # for each frame, update the data stored on each artist.
    simulator.evolve(0.01)
    x = simulator.particle.x
    y = simulator.particle.y
    # update the line plot:
    line.set_xdata(simulator.particle.x)
    line.set_ydata(y = simulator.particle.y)
    return line


anim = animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=10)
plt.show()

