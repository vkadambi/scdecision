#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Date            Programmers                         Descriptions of Change
# ====         ================                       ======================
# 08/15/19        Vai                                 Original code
# 08/15/19.       Vai                                 Main includes function call/plots
# 08/18/19        Vai                                 Regular Histograms generated!
# 08/19/19        Vai                                 Add Runtimes

np.random.seed(0)
from ugm_diffusion import stone,stoneUGM,stoneEta,stoneEtaUGM,ratcliff,ratcliffUGM

#Stone function call
data_stone = stone(0.5,1,1,0,1,0.001,100,10000)
numnans_stone = np.sum(np.isnan(data_stone))
data_stone = np.array(data_stone)
#Stone plot
plt.figure(1)
sns.distplot(data_stone[np.logical_not(np.isnan(data_stone))], hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('Density Plot & Histogram of Stone Data')
plt.xlabel('Reaction Times')
plt.ylabel('Frequency')
plt.savefig("stone.png")

#StoneUGM function call
data_stoneUGM = stoneUGM(0.5,1,1,0,1,1,1,0.001,100,1000)
#StoneUGM plot
plt.figure(2)
sns.distplot(data_stoneUGM, hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('Density Plot & Histogram of StoneUGM Data')
plt.xlabel('Reaction Times')
plt.ylabel('Frequency')
plt.savefig("stoneUGM.png")

#StoneEta function call
data_stoneEta = stoneEta(0.5,1,1,1,0,1,0.001,100,1000)
#StoneEta plot
plt.figure(3)
sns.distplot(data_stoneEta, hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('Density Plot & Histogram of StoneEta Data')
plt.xlabel('Reaction Times')
plt.ylabel('Frequency')
plt.savefig("stoneEta.png")

#StoneEtaUGM function call
data_EtaUGM = stoneEtaUGM(0.5,1,1,1,0,1,1,1,0.001,100,1000)
#StoneEtaUGM plot
plt.figure(4)
sns.distplot(data_EtaUGM, hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('Density Plot & Histogram of StoneEtaUGM Data')
plt.xlabel('Reaction Times')
plt.ylabel('Frequency')
plt.savefig("stoneEtaUGM.png")

#RatCliff function call
data_ratcliff = ratcliff(0,1,1,1,0,1,1,0.001,100,1000)
#RatCliff plot
plt.figure(5)
sns.distplot(data_ratcliff, hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('Density Plot & Histogram of RatCliff Data')
plt.xlabel('Reaction Times')
plt.ylabel('Frequency')
plt.savefig("ratcliff.png")

#RatCliffUGM function call
data_ratcliffUGM = ratcliffUGM(0,1,1,1,0,1,1,1,1,0.001,100,1000)
#RatCliffUGM plot
plt.figure(6)
sns.distplot(data_ratcliffUGM, hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('Density Plot & Histogram of RatCliffUGM Data')
plt.xlabel('Reaction Times')
plt.ylabel('Frequency')
plt.savefig("ratcliffUGM.png")
