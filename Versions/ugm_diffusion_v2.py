import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import random

# Date            Programmers                         Descriptions of Change
# ====         ================                       ======================
# 08/15/19        Vai                              Original code

def stone (z,v,aU,aL,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp=[]
    rt=[]
    #evidence = np.empty((maxiter,n))
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        x=z
        iter=0
        # resp.append(np.nan) #Delete this
        while (iter<=Maxiter): #Note difference here
            nDots = nDotsVector[iter]
            iter=iter+1
            x=x+h*(v*nDots)+rhs*np.random.normal()
            # evidence[iter-1,i] = x
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
    data=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    #Get rid of this
    # result=pd.Series(data) #what exactly is Series in Panda
    # result.plot.hist(grid=True, bins=1, rwidth=0.9,color='#607c8e')
    # plt.title('Stone Data')
    # plt.xlabel('Counts')
    # plt.ylabel('Reaction Times')
    # plt.grid(axis='y', alpha=0.75)
    # plt.savefig("stone.png")
    print (data)
    return resp, rt, data #Return all three to test
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
    data=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    result=pd.Series(data) #what exactly is Series in Panda
    result.plot.hist(grid=True, bins=1, rwidth=0.9,color='#607c8e')
    plt.title('Stone Data')
    plt.xlabel('Counts')
    plt.ylabel('Reaction Times')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig("stoneUGM.png")
    print (data)
    return data
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
    data=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    result=pd.Series(data) #what exactly is Series in Panda
    result.plot.hist(grid=True, bins=1, rwidth=0.9,color='#607c8e')
    plt.title('Stone Data')
    plt.xlabel('Counts')
    plt.ylabel('Reaction Times')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig("stoneEta.png")
    print (data)
    return data
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
    data=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    result=pd.Series(data) #what exactly is Series in Panda
    result.plot.hist(grid=True, bins=1, rwidth=0.9,color='#607c8e')
    plt.title('Stone Data')
    plt.xlabel('Counts')
    plt.ylabel('Reaction Times')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig("ratcliff.png")
    print (data)
    return data
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
    data=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    result=pd.Series(data) #what exactly is Series in Panda
    result.plot.hist(grid=True, bins=1, rwidth=0.9,color='#607c8e')
    plt.title('Stone Data')
    plt.xlabel('Counts')
    plt.ylabel('Reaction Times')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig("ratcliff.png")
    print (data)
    return data
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
    data=[]
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    result=pd.Series(data) #what exactly is Series in Panda
    result.plot.hist(grid=True, bins=1, rwidth=0.9,color='#607c8e')
    plt.title('Stone Data')
    plt.xlabel('Counts')
    plt.ylabel('Reaction Times')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig("ratcliffUGM.png")
    print (data)
    return data
