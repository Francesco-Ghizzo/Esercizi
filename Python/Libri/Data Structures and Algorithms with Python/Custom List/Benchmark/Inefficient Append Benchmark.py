#!/usr/bin/env python
# coding: utf-8


import datetime

import random

import time


import matplotlib.pyplot as plt



# Create a Python list with all numbers from 1 to 1000:


xmin = 1

xmax = 1000


xList = []


for x in range(xmin, xmax+1):
    xList.append(x)



# Custom class PyList:


class PyList: 
    def __init__(self):
        self.items = []
    def inefficientAppend(self, item):
            self.items = self.items + [item]



# initialize an object of the class PyList:


xList = PyList()



## Benchmark how the time required to append n elements in a list grows as n grows larger


# Inefficient append:


inefficientTimes = [0]*xmax


for x in range(xmin, xmax+1):
    xList = PyList()
    starttime = datetime.datetime.now()
    for i in range(xmin, x):
        xList.inefficientAppend(x)
    endtime = datetime.datetime.now()
    deltaT = endtime - starttime
    accessTime = deltaT.total_seconds()*10**6    # tempo em microsegundos
    inefficientTimes[x-1] = accessTime


# Plot:


fig, ax = plt.subplots(layout='constrained')
ax.plot(inefficientTimes, label='Inefficient Append')
ax.set_xlabel('list size (number of elements)')
ax.set_ylabel('time (µs)')
ax.set_title("Inefficient Append")
ax.legend()



# Default Python append:


defaultTimes = [0]*xmax


for x in range(xmin, xmax+1):
    xList = []
    starttime = datetime.datetime.now()
    for i in range(xmin, x):
        xList.append(x)
    endtime = datetime.datetime.now()
    deltaT = endtime - starttime
    accessTime = deltaT.total_seconds()*10**6    # tempo em microsegundos
    defaultTimes[x-1] = accessTime


# Plot:


fig, ax = plt.subplots(layout='constrained')
ax.plot(defaultTimes, label='Default Append')
ax.set_xlabel('list size (number of elements)')
ax.set_ylabel('time (µs)')
ax.set_title("Default Append")
ax.legend()



# Default Python append implemented in custom PyList:


class PyList: 
    def __init__(self):
        self.items = []
    def defaultAppend(self, item):
        self.items.append(item)


for x in range(xmin, xmax+1):
    xList = PyList()
    starttime = datetime.datetime.now()
    for i in range(xmin, x):
        xList.defaultAppend(x)
    endtime = datetime.datetime.now()
    deltaT = endtime - starttime
    accessTime = deltaT.total_seconds()*10**6    # tempo em microsegundos
    defaultTimes[x-1] = accessTime


# Plot:


fig, ax = plt.subplots(layout='constrained')
ax.plot(defaultTimes, label='Default Append')
ax.set_xlabel('list size (number of elements)')
ax.set_ylabel('time (µs)')
ax.set_title("Default Append")
ax.legend()



# Default Python append vs Inefficient append


fig, ax = plt.subplots(layout='constrained')
ax.plot(inefficientTimes, label='Inefficient Append')
ax.plot(defaultTimes, label='Default Append')
ax.set_xlabel('list size (number of elements)')
ax.set_ylabel('time (µs)') 
ax.set_title("Default vs Inefficient Append")
ax.legend()

