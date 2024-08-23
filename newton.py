import warnings
import autograd.numpy as np
import math

def dev (f):
    fd_fuc = np.derivative(f)
    return(fd_fuc)

def sec_dev(f, x0):
    result = np.derivative(f, x0)
    return(result)

def newtons_method(x0, function):
    t = 0 # iteration start point
    xt = 0
    while(abs(x0 - xt) > 0):
        xt = x0 - dev(x0)/dev(dev(x0))
        t = t + 1 # update every step (increasing)?

    return(result)
