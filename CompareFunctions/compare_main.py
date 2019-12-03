import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
np.random.seed(0)
from compare_function_stone import stone, simuldiffn200
from compare_function_Eta import stoneEta, simuldiffn200

#defining parameters
#diffusion coefficient
tester_s = round(np.random.uniform(0,1),0)
if (tester_s == 0.0):
    s = 0.1
    aU = 0.1
elif (tester_s == 1.0):
    s = 1.0
    aU = 1.0
#drift rate
if (s == 0.1):
    v = np.random.uniform(-0.9,0.9)
elif (s == 1.0):
    v = np.random.uniform(-9,9)
#bias
z = np.random.uniform(0,aU)
beta = z/aU
#trial variability of the drift rate
Eta = np.random.uniform(0,2)
#urgency signal
usign = np.random.uniform(1,2)
#time resolution
h = 0.001
#number of trials, changed from 100
n = 10000
#number of steps
maxiter = 1000
#range of Zeta
rangeZeta = np.random.uniform(0.45,0.55)


#Stone function call
data_stone = stone(beta,v,aU,s,h,n,maxiter)
data_stone = np.array(data_stone)

# StoneEta function call
data_stone_eta = stoneEta(beta,v,Eta,aU,s,h,n,maxiter)
data_stone_eta = np.array(data_stone_eta)

# simuldiffn200 function call (stone)
data_mic_stone = simuldiffn200(beta,n,aU,0,0,v,None,0,0,rangeZeta,0,s)
data_mic_stone = np.array(data_mic_stone)

# simuldiffn200 function call (stoneEta)
data_mic_Eta = simuldiffn200(beta,n,aU,0,0,v,None,0,0,rangeZeta,Eta,s)
data_mic_Eta = np.array(data_mic_Eta)

#Stone plot
plt.figure(1)
sns.distplot(data_stone[~np.isnan(data_stone)], hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
sns.distplot(data_mic_stone[~np.isnan(data_mic_stone)], hist=True, kde=True,bins=int(180/5), color = 'purple',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('Comparsion of the Stone Programs')
plt.xlabel('Reaction Times')
plt.ylabel('Frequency')
plt.savefig("stone_compare.png")

#StoneEta plot
plt.figure(2)
sns.distplot(data_stone_eta[~np.isnan(data_stone_eta)], hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
sns.distplot(data_mic_Eta[~np.isnan(data_mic_Eta)], hist=True, kde=True,bins=int(180/5), color = 'purple',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('Comparsion of the StoneEta Programs')
plt.xlabel('Reaction Times')
plt.ylabel('Frequency')
plt.savefig("stoneEta_compare.png")

#go through a bunch of different drift rates and see i

#shift curve so that we can see both lines
#shortcut for generating simulations from the paper
#does hddm require a dataframe or can you just use vectors 
