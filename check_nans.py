#!/usr/bin/python
import numpy as np
#Questions
# how many decimals should we round to
np.random.seed(0)
from ugm_diffusion import stone,stoneUGM,stoneEta,stoneEtaUGM,ratcliff,ratcliffUGM

def random_parameter() :
    #upper boundary
    aU = round(np.random.uniform(0.7,1.5),2)
    #bias
    z = np.random.uniform(0,aU)
    beta = round((z/aU),2)
    #diffusion coefficient
    tester_s = round(np.random.uniform(0,1),0)
    if (tester_s == 0.0):
        s = 0.1
    elif (tester_s == 1.0):
        s = 1.0
    #drift rate
    if (s == 0.1):
        v = round(np.random.uniform(-0.9,0.9),2)
    elif (s == 1.0):
        v = round(np.random.uniform(-9,9),2)
    usign = 1
    eta = 1
    return beta,aU,s,v,usign,eta

#generate all the random variables
beta,aU,s,v,usign,eta = random_parameter()
h = 0.001 #time resolution
n = 100 #number of trials
maxiter = 1000 #number of steps
timecons = 1000
zmin = 0
zmax = 1

#checking all the functions
data_stone = stone(beta,v,aU,s,h,n,maxiter)
data_stone_check = np.isnan(data_stone)
for i in range(len(data_stone_check)):
    if i is False:
        print ("stone NANS :",beta,v,aU,s)
data_stoneUGM = stoneUGM (beta,v,aU,timecons,usign,s,h,n,maxiter)
data_stoneUGM_check = np.isnan(data_stoneUGM)
for i in range(len(data_stoneUGM_check)):
    if i is False:
        print ("stoneUGM NANS:",beta,v,aU,timecons,usign,s)
data_stoneEta = stoneEta (beta,v,eta,aU,s,h,n,maxiter)
data_stoneEta_check = np.isnan(data_stoneEta)
for i in range(len(data_stoneEta_check)):
    if i is False:
        print ("stoneEta NANS:",beta,v,eta,aU,s)
data_EtaUGM = stoneEtaUGM (beta,v,eta,aU,timecons,usign,s,h,n,maxiter)
data_EtaUGM_check = np.isnan(data_EtaUGM)
for i in range(len(data_EtaUGM_check)):
    if i is False:
        print ("EtaUGM NANS:",beta,v,eta,aU,timecons,usign,s)
data_ratcliff = ratcliff (zmin,zmax,v,aU,eta,s,h,n,maxiter)
data_ratcliff_check = np.isnan(data_ratcliff)
for i in range(len(data_ratcliff_check)):
    if i is False:
        print ("ratcliff NANS:",v,aU,eta,s)
data_ratcliffUGM = ratcliffUGM (zmin,zmax,v,aU,eta,timecons,usign,s,h,n,maxiter)
data_ratcliffUGM_check = np.isnan(data_ratcliffUGM)
for i in range(len(data_ratcliffUGM_check)):
    if i is False:
        print ("ratcliffUGM NANS:",v,aU,eta,timecons,usign,s)

#worked out well, print the variables
print("All good!",beta,",",v,",",eta,",",aU,",",timecons,",",usign,",",s)

