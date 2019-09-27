#!/usr/bin/python
import numpy as np

from ugm_diffusion import stone,stoneUGM,stoneEta,stoneEtaUGM,ratcliff,ratcliffUGM

def random_parameter() :
    #upper boundary
    aU = np.random.uniform(0.7,1.5)
    #bias
    z = np.random.uniform(0,aU)
    beta = z/aU
    #diffusion coefficient
    tester_s = np.random.uniform(0,1)
    if (tester_s == 0.0):
        s = 0.1
    elif (tester_s == 1.0):
        s = 1.0
    #drift rate
    if (s == 0.1):
        v = np.random.uniform(-0.9,0.9)
    elif (s == 1.0):
        v = np.random.uniform(-9,9)
    #trial variability of the drift rate
    eta = np.random.uniform(0,2)
    #urgency signal
    usign = np.random.uniform(1,2)
    #time resolution
    h = 0.001
    #number of trials
    n = 100
    #number of steps
    maxiter = 1000
    #descirbes the leak
    timecons = 1000
    # bias min and max
    zmin = 0
    zmax = 1

    #return the random parameter
    return beta,zmin,zmax,v,eta,aU,timecons,usign,s,h,n,maxiter

for i in range (1) :
    #generate all the random variables
    beta,zmin,zmax,v,eta,aU,timecons,usign,s,h,n,maxiter = random_parameter()
    #checking all the functions
    data_stone = stone(beta,v,aU,s,h,n,maxiter)
    data_stone_check = np.isnan(data_stone)
    for i in range(len(data_stone_check)):
        if (data_stone_check[i]==True):
            print ("stone NANS :",beta,v,aU,s,h,n,maxiter)
            break
    data_stoneUGM = stoneUGM (beta,v,aU,timecons,usign,s,h,n,maxiter)
    data_stoneUGM_check = np.isnan(data_stoneUGM)
    for i in range(len(data_stoneUGM_check)):
        if (data_stoneUGM_check[i]==True):
            print ("stoneUGM NANS:",beta,v,aU,timecons,usign,s,h,n,maxiter)
            break
    data_stoneEta = stoneEta (beta,v,eta,aU,s,h,n,maxiter)
    data_stoneEta_check = np.isnan(data_stoneEta)
    for i in range(len(data_stoneEta_check)):
        if (data_stoneEta_check[i]==True):
            print ("stoneEta NANS:",beta,v,eta,aU,s,h,n,maxiter)
            break
    data_EtaUGM = stoneEtaUGM (beta,v,eta,aU,timecons,usign,s,h,n,maxiter)
    data_EtaUGM_check = np.isnan(data_EtaUGM)
    for i in range(len(data_EtaUGM_check)):
        if (data_EtaUGM_check[i]==True):
            print ("EtaUGM NANS:",beta,v,eta,aU,timecons,usign,s,h,n,maxiter)
            break
    data_ratcliff = ratcliff (zmin,zmax,v,aU,eta,s,h,n,maxiter)
    data_ratcliff_check = np.isnan(data_ratcliff)
    for i in range(len(data_ratcliff_check)):
        if (data_ratcliff_check[i]==True):
            print ("ratcliff NANS:",zmin,zmax,v,aU,eta,s,h,n,maxiter)
            break
    data_ratcliffUGM = ratcliffUGM (zmin,zmax,v,aU,eta,timecons,usign,s,h,n,maxiter)
    data_ratcliffUGM_check = np.isnan(data_ratcliffUGM)
    for i in range(len(data_ratcliffUGM_check)):
        if (data_ratcliffUGM_check[i]==True):
            print ("ratcliffUGM NANS:",zmin,zmax,v,aU,eta,timecons,usign,s,h,n,maxiter)
            break

#worked out well, print the variables
print("All good!")
