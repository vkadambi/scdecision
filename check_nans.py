#!/usr/bin/python
import numpy as np

np.random.seed(0)
from ugm_diffusion import stone,stoneUGM,stoneEta,stoneEtaUGM,ratcliff,ratcliffUGM

#parameter definitions - that can change
z = 0.5 #bias
v = -1 #drift rate between -.9 to .9 or -9 to 9 depending on s
aU = 0.7 #lower limit is always 0 (0.7 to 1.5)
aL = 0 #lower limit is always 0
s = 0.1 #diffusion coefficient 0.1 or 1

#parameter definitions - that cannot change
h = 0.001 #time resolution
n = 100 #number of trials
maxiter = 1000 #number of steps
timecons = 1
usign = 1
eta = 1
zmin = 0
zmax = 1

data_stone = stone(z,v,aU,aL,s,h,n,maxiter)
data_stone_check = np.isnan(data_stone)
for i in range(len(data_stone_check)):
    if i is False:
        print ("stone NANS")
data_stoneUGM = stoneUGM(z,v,aU,aL,timecons,usign,s,h,n,maxiter)
data_stoneUGM_check = np.isnan(data_stoneUGM)
for i in range(len(data_stoneUGM_check)):
    if i is False:
        print ("stoneUGM NANS")
data_stoneEta = stoneEta(z,v,eta,aU,aL,s,h,n,maxiter)
data_stoneEta_check = np.isnan(data_stoneEta)
for i in range(len(data_stoneEta_check)):
    if i is False:
        print ("stoneEta NANS")
data_EtaUGM = stoneEtaUGM(z,v,eta,aU,aL,timecons,usign,s,h,n,maxiter)
data_EtaUGM_check = np.isnan(data_EtaUGM)
for i in range(len(data_EtaUGM_check)):
    if i is False:
        print ("EtaUGM NANS")
data_ratcliff = ratcliff(zmin,zmax,v,aU,aL,eta,s,h,n,maxiter)
data_ratcliff_check = np.isnan(data_ratcliff)
for i in range(len(data_ratcliff_check)):
    if i is False:
        print ("ratcliff NANS")
data_ratcliffUGM = ratcliffUGM(zmin,zmax,v,aU,aL,eta,timecons,usign,s,h,n,maxiter)
data_ratcliffUGM_check = np.isnan(data_ratcliffUGM)
for i in range(len(data_ratcliffUGM_check)):
    if i is False:
        print ("ratcliffUGM NANS")

