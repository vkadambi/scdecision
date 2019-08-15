#!/usr/bin/python 
import numpy as np
np.random.seed(0)                                          
from ugm_diffusion_v2 import stone,stoneUGM,stoneEta,stoneEtaUGM,ratcliff,ratcliffUGM
stone(0.5,1,1,0,1,0.1,100,1000)
stoneUGM(0.5,1,1,0,1,1,1,0.1,100,1000)
stoneEta(0.5,1,1,1,0,1,0.1,100,1000)
stoneEtaUGM(0.5,1,1,1,0,1,1,1,0.1,100,1000)
ratcliff(0,1,1,1,0,1,1,0.1,100,1000)
ratcliffUGM(0,1,1,1,0,1,1,1,1,0.1,100,1000)
