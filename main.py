#!/usr/bin/python
from ugm_diffusion import stone,stoneUGM,stoneEta,stoneEtaUGM,ratcliff,ratcliffUGM 

stone(1,5,1,0,1,1,5,5)
stoneUGM(1,5,1,0,1,1,1,1,5,5)
stoneEta(1,5,1,1,0,1,1,5,5)
stoneEtaUGM(1,5,1,1,0,1,1,1,1,5,5)
ratcliff(1,2,5,1,0,1,1,1,5,5)
ratcliffUGM(1,2,5,1,0,1,1,1,1,1,5,5)
