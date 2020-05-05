import numpy as np
import math
import random

def random_parameter() :
    #diffusion coefficient
    s = 1.0
    #drift rate
    v = np.random.uniform(-4,4)
    #upper boundary
    aU = np.random.uniform(0.4,2.0)
    #bias
    beta = 0.5
    #time resolution
    h = 0.001
    #number of trials
    n = 100
    #number of steps
    maxiter = 1000
    #trial variability of the drift rate
    eta = np.random.uniform(0,2)
    #return random parameters
    return beta,v,aU,s,h,n,eta,maxiter
