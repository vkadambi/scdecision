import time
import numpy as np 
np.random.seed(0)

from ugm_diffusion import stone,stoneUGM,stoneEta,stoneEtaUGM,ratcliff,ratcliffUGM

#Stone Runtime
start_time_stone = time.time()
stone(0.5,1,1,0,1,0.1,100,1000)
print("%s seconds -- Stone" % (time.time() - start_time_stone))

#StoneUGM Runtime
start_time_stoneUGM = time.time()
stoneUGM(0.5,1,1,0,1,1,1,0.1,100,1000)
print("%s seconds -- StoneUGM" % (time.time() - start_time_stoneUGM))

#StoneEta Runtime
start_time_stoneEta = time.time()
stoneEta(0.5,1,1,1,0,1,0.1,100,1000)
print("%s seconds -- StoneEta" % (time.time() - start_time_stoneEta))

#StoneEtaUGM Runtime
start_time_stoneEtaUGM = time.time()
stoneEtaUGM(0.5,1,1,1,0,1,1,1,0.1,100,1000)
print("%s seconds -- StoneEtaUGM" % (time.time() - start_time_stoneEtaUGM))

#RatCliff Runtime
start_time_ratcliff = time.time()
ratcliff(0,1,1,1,0,1,1,0.1,100,1000)
print("%s seconds -- RatCliff" % (time.time() - start_time_ratcliff))

#RatCliffUGM Runtime
start_time_ratcliffUGM = time.time()
ratcliffUGM(0,1,1,1,0,1,1,1,1,0.1,100,1000)
print("%s seconds -- RatCliffUGM" % (time.time() - start_time_ratcliffUGM))

