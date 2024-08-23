import numpy as np
import math

def dev (f):
    fd_fuc = np.derivative(f)
    return(fd_fuc)

def newtons_method(x0, function, eps=1e-5):
    t = 0 # iteration start point
    xt = float("inf")
    while(abs(x0 - xt) > eps):
        xt = x0 - dev(x0)/dev(dev(x0))
        t = t + 1 # update every step (increasing)?

    return(result)
