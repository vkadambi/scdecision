#!/usr/bin/python
import numpy as np

np.random.seed(0)
from ugm_diffusion import stone,stoneUGM,stoneEta,stoneEtaUGM,ratcliff,ratcliffUGM

data_stone = stone(0.5,1,1,0,1,0.001,100,1000)
data_stone_check = np.isnan(data_stone)
for i in range(len(data_stone_check)):
    if i is False:
        print ("stone NANS")
data_stoneUGM = stoneUGM(0.5,1,1,0,1,1,1,0.001,100,1000)
data_stoneUGM_check = np.isnan(data_stoneUGM)
for i in range(len(data_stoneUGM_check)):
    if i is False:
        print ("stoneUGM NANS")
data_stoneEta = stoneEta(0.5,1,1,1,0,1,0.001,100,1000)
data_stoneEta_check = np.isnan(data_stoneEta)
for i in range(len(data_stoneEta_check)):
    if i is False:
        print ("stoneEta NANS")
data_EtaUGM = stoneEtaUGM(0.5,1,1,1,0,1,1,1,0.001,100,1000)
data_EtaUGM_check = np.isnan(data_EtaUGM)
for i in range(len(data_EtaUGM_check)):
    if i is False:
        print ("EtaUGM NANS")
data_ratcliff = ratcliff(0,1,1,1,0,1,1,0.001,100,1000)
data_ratcliff_check = np.isnan(data_ratcliff)
for i in range(len(data_ratcliff_check)):
    if i is False:
        print ("ratcliff NANS")
data_ratcliffUGM = ratcliffUGM(0,1,1,1,0,1,1,1,1,0.001,100,1000)
data_ratcliffUGM_check = np.isnan(data_ratcliffUGM)
for i in range(len(data_ratcliffUGM_check)):
    if i is False:
        print ("ratcliffUGM NANS")

