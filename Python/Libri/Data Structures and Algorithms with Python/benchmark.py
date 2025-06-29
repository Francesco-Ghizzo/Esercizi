import datetime
import random
import time

def benchmark(func, *args):
    starttime = datetime.datetime.now()
        func(*args)
    endtime = datetime.datetime.now()
    deltaT = endtime - starttime
        return deltaT
