#!/usr/bin/python 
import numpy as np
import matplotlib.pyplot as plt #Add this
import seaborn as sns #Add this

np.random.seed(0)                                          
from ugm_diffusion_v2 import stone,stoneUGM,stoneEta,stoneEtaUGM,ratcliff,ratcliffUGM
resp, rt, data = stone(0.5,1,1,0,1,0.1,100,1000) #Add outputs
# stone(0.5,1,1,0,1,0.1,100,1000)

plt.figure()
result=pd.Series(data) #what exactly is Series in Panda
result.plot.hist(grid=True, bins=1, rwidth=0.9,color='#607c8e')
plt.title('Stone Data')
plt.xlabel('Counts')
plt.ylabel('Reaction Times')
plt.grid(axis='y', alpha=0.75)
plt.savefig("stone.png")

resp, rt, data = stoneUGM(0.5,1,1,0,1,1,1,0.1,100,1000) #Add outputs

plt.figure()

stoneEta(0.5,1,1,1,0,1,0.1,100,1000)
stoneEtaUGM(0.5,1,1,1,0,1,1,1,0.1,100,1000)
ratcliff(0,1,1,1,0,1,1,0.1,100,1000)
ratcliffUGM(0,1,1,1,0,1,1,1,1,0.1,100,1000)
