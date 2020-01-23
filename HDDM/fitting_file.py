import pandas as pd
import matplotlib.pyplot as plt
import hddm
import numpy as np
import math
import random
import seaborn as sns
import csv

#first define the stone function
def stone (beta,v,aU,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp = []
    rt = []
    data = []
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        x=beta*aU
        iter=0
        while (iter<=Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x=x+h*(v*nDots)+rhs*np.random.normal()
            if (x>=aU):
                resp.append(float(1.0))
                break
            if (x<=0):
                resp.append(float(-1.0))
                break
            if (iter==Maxiter):
                resp.append(np.nan)
                break
        number=((float(iter))*h)-(h/(float(2.0)))
        rt.append(number)
    for i in range(N):
        temp=resp[i]*rt[i]
        data.append(temp)
    return data
    
# generate the data we want using a set of defined parameters, take out the Nans

np.random.seed(0)
data = np.array(stone(0.5,1,1,1,0.001,100,1000))
data = data[~np.isnan(data)]

# create an array for the response (1 for positive and 0 for negative)
response = []
for i in data:
    if (i > 0 ):
        response.append(1)
    elif (i < 0):
        response.append(0)
response = np.array(response)

# since we have the response data, we use the absolute value for the rts
for i in range(len(data)):
    data[i] = abs(data[i])

#put the array into a csv file
data_csv = csv.writer(open ('data.csv', 'w'), delimiter=',', lineterminator='\n')
data_csv.writerow(['rt','response'])
for i in range(len(data)):
    list = [data[i],response[i]]
    data_csv.writerows([list])

#plot for fun
plt.figure(1)
sns.distplot(data[~np.isnan(data)], hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('HDDM Graph')
plt.xlabel('Reaction Times')
plt.ylabel('Frequency')
plt.savefig("stone.png")

# load the data from the data.csv file into a variable data_stone
#data_stone = hddm.load_csv('data.csv')

#data_stone = hddm.utils.flip_errors(data_stone)

# Instantiate model object passing it data_stone
# This will tailor an individual hierarchical DDM around the dataset.
#m = hddm.HDDM(data_stone)

# find a good starting point which helps with convergence
#starting_values = m.find_starting_values()

# start drawing 7000 samples and discarding 5000 as burn-in
#m.sample(2000, burn=20)

# Now we have an estimated model. We are going to print a summary stats table for each parameters' posterior.

#stats = m.gen_stats()
#stats[stats.index.isin(['a', 'a_std', 'a_subj.0', 'a_subj.1'])]

#plt.figure(3)
#m.plot_posterior_predictive(figsize=(14, 10))
#plt.savefig("predictive.png")

