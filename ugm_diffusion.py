import numpy as np
#import numpy.ma as ma 
import math
import random
def stone (z,v,aU,aL,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp=[]
    rt=[]
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        x=z
        iter=0
        resp.append(np.nan)
        while (iter<Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x=x+h*(v*nDots)+rhs*np.random.normal()
            if (x>=aU):
                resp.append(float(-1.0))
                break
            if (x<=aL):
                resp.append(float(1.0))
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    result=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        result.append(temp)
    return result
def stoneUGM (z,v,aU,aL,timecons,usign,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp=[]
    rt=[]
    nDotsVector=np.ones(Maxiter)
    # weight for expotentionally-weighted moving average 
    # alpha = (h)/(h+timecons)
    alpha = timecons/(timecons+h)
    for i in range(N):
        x=z
        iter=0
        resp.append(np.nan)
        while (iter<Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            #filtered signal from previous step + input from current step 
            x=(alpha*x)+(1-alpha)*(h*(v*nDots))+rhs*np.random.normal()
            # multiply linear urgency signal, urgency determines size of urgency signal 
            xu =x*iter*(usign) #urgency is multiplicative 
            if (x>=aU):
                resp.append(float(-1.0))
                break
            if (x<=aL):
                resp.append(float(1.0))
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    result=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        result.append(temp)
    return result
def stoneEta (z,v,eta,aU,aL,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp=[]
    rt=[]
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        samplev=v+eta*np.random.normal()
        x=z
        iter=0
        resp.append(np.nan)
        while (iter<Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x=x+h*(samplev*nDots)+rhs*np.random.normal()
            if (x>=aU):
                resp.append(float(-1.0))
                break
            if (x<=aL):
                resp.append(float(1.0))
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    result=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        result.append(temp)
    return result
def stoneEtaUGM (z,v,eta,aU,aL,timecons,usign,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s 
    resp=[]
    rt=[]
    nDotsVector=np.ones(Maxiter)    
    #weight for exponentially-weighted moving average
    #alpha=(*h)/((*h)+(*imecons));
    alpha=(timecons)/(timecons+h)
    for i in range(N):
        samplev=v+eta*np.random.normal()
        x=z
        iter=0
        resp.append(np.nan)
        while (iter<Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x = alpha*x+(1-alpha)*(h*(samplev*nDots))+rhs*np.random.normal()
            xu=x*iter*usign
            if (x>=aU):
                resp.append(float(-1.0))
                break
            if (x<=aL):
                resp.append(float(1.0))
                break      
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    result=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        result.append(temp)
    return result
def ratcliff (zmin,zmax,v,aU,aL,eta,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp=[]
    rt=[]
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        samplev=v+eta*np.random.normal()
        x=zmin+(zmax-zmin)*np.random.uniform()
        iter=0
        resp.append(np.nan)
        while (iter<Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x = x+h*(samplev*nDots)+rhs*np.random.normal()
            if (x>=aU):
                resp.append(float(-1.0))
                break
            if (x<=aL):
                resp.append(float(1.0))
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    result=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        result.append(temp)
    return result
def ratcliffUGM (zmin,zmax,v,aU,aL,eta,timecons,usign,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp=[]
    rt=[]
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        samplev=v+eta*np.random.normal()
        x=zmin+(zmax-zmin)*np.random.uniform()
        iter=0
        resp.append(np.nan)
        while (iter<Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x = x+h*(samplev*nDots)+rhs*np.random.normal()
            xu=x*iter*usign
            if (x>=aU):
                resp.append(float(-1.0))
                break
            if (x<=aL):
                resp.append(float(1.0))
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    result=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        result.append(temp)
    return result
