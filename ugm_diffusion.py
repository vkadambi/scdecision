import numpy as np
import math
import random

# Date            Programmers                         Descriptions of Change
# ====         ================                       ======================
# 08/15/19        Vai                                 Original code

def stone (z,v,aU,aL,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp = []
    rt = []
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        x=z
        iter=0
        while (iter<=Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x=x+h*(v*nDots)+rhs*np.random.normal()
            if (x>=aU):
                resp.append(float(1.0))
                break
            if (x<=aL):
                resp.append(float(-1.0))
                break
            if (iter==Maxiter):
                resp = np.array(resp)
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    data = []
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    print (data)
    return resp, rt, data #Return all three to test
def stoneUGM (z,v,aU,aL,timecons,usign,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp = []
    rt = []
    nDotsVector=np.ones(Maxiter)
    # weight for expotentionally-weighted moving average
    # alpha = (h)/(h+timecons)
    alpha = timecons/(timecons+h)
    for i in range(N):
        x=z
        iter=0
        while (iter<=Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            #filtered signal from previous step + input from current step
            x=(alpha*x)+(1-alpha)*(h*(v*nDots))+rhs*np.random.normal()
            # multiply linear urgency signal, urgency determines size of urgency signal
            xu =x*iter*(usign) #urgency is multiplicative
            if (x>=aU):
                resp.append(float(1.0)) #This switch is convention
                break
            if (x<=aL):
                resp.append(float(-1.0)) #This switch is convention
                break
            if (iter==Maxiter): #New if statement
                resp.append(np.nan)
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    data = []
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    print (data)
    return resp, rt, data #Return all three to test
def stoneEta (z,v,eta,aU,aL,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp = []
    rt = []
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        samplev=v+eta*np.random.normal()
        x=z
        iter=0
        while (iter<=Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x=x+h*(samplev*nDots)+rhs*np.random.normal()
            if (x>=aU):
                resp.append(float(1.0)) #This switch is convention
                break
            if (x<=aL):
                resp.append(float(-1.0)) #This switch is convention
                break
            if (iter==Maxiter): #New if statement
                resp.append(np.nan)
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    data = []
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    print (data)
    return resp, rt, data #Return all three to test
def stoneEtaUGM (z,v,eta,aU,aL,timecons,usign,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp = []
    rt = []
    nDotsVector=np.ones(Maxiter)
    #weight for exponentially-weighted moving average
    #alpha=(*h)/((*h)+(*imecons));
    alpha=(timecons)/(timecons+h)
    for i in range(N):
        samplev=v+eta*np.random.normal()
        x=z
        iter=0
        resp.append(np.nan)
        while (iter<=Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x = alpha*x+(1-alpha)*(h*(samplev*nDots))+rhs*np.random.normal()
            xu=x*iter*usign
            if (x>=aU):
                resp.append(float(1.0)) #This switch is convention
                break
            if (x<=aL):
                resp.append(float(-1.0)) #This switch is convention
                break
            if (iter==Maxiter): #New if statement
                resp.append(np.nan)
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    data = []
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    print (data)
    return resp, rt, data #Return all three to test
def ratcliff (zmin,zmax,v,aU,aL,eta,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp = []
    rt = []
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        samplev=v+eta*np.random.normal()
        x=zmin+(zmax-zmin)*np.random.uniform()
        iter=0
        while (iter<=Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x = x+h*(samplev*nDots)+rhs*np.random.normal()
            if (x>=aU):
                resp.append(float(1.0)) #This switch is convention
                break
            if (x<=aL):
                resp.append(float(-1.0)) #This switch is convention
                break
            if (iter==Maxiter): #New if statement
                resp.append(np.nan)
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    data = []
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    print (data)
    return resp, rt, data #Return all three to test
def ratcliffUGM (zmin,zmax,v,aU,aL,eta,timecons,usign,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp = []
    rt = []
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        samplev=v+eta*np.random.normal()
        x=zmin+(zmax-zmin)*np.random.uniform()
        iter=0
        while (iter<=Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x = x+h*(samplev*nDots)+rhs*np.random.normal()
            xu=x*iter*usign
            if (x>=aU):
                resp.append(float(1.0)) #This switch is convention
                break
            if (x<=aL):
                resp.append(float(-1.0)) #This switch is convention
                break
            if (iter==Maxiter): #New if statement
                resp.append(np.nan)
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    data = []
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    print (data)
    return resp, rt, data #Return all three to test
