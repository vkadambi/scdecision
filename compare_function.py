import numpy as np
import math
import random

def stone (beta=0.5,v=1,aU=1,s=1,h=0.001,n=100,maxiter=1000) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp = []
    rt = []
    data = []
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        x=beta*aU
        iter=0
        while (iter<=Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x=x+h*(v*nDots)+rhs*np.random.normal()
            if (x>=aU):
                resp.append(float(1.0))
                break
            if (x<=0):
                resp.append(float(-1.0))
                break
            if (iter==Maxiter):
                resp.append(np.nan)
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    return data
