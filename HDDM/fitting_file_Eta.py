import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import seaborn as sns
import csv
import hddm
import scipy.io as sio
from scipy import stats as scipy_stats
from IPython import get_ipython  # Run magic functions from script
get_ipython().magic('pylab')  # Initialize ipython matplotlib plotting graphics

def stoneEta (beta,v,eta,aU,s,h,n,maxiter) :
    N = int(n)
    Maxiter = int(maxiter)
    rhs = (math.sqrt(h))*s
    resp = []
    rt = []
    data = []
    nDotsVector=np.ones(Maxiter)
    for i in range(N):
        samplev=v+eta*np.random.normal()
        x=beta*aU
        iter=0
        while (iter<=Maxiter):
            nDots = nDotsVector[iter]
            iter=iter+1
            x=x+h*(samplev*nDots)+rhs*np.random.normal()
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

def random_parameter() :
    #diffusion coefficient
    s = 1.0
    #drift rate
    v = np.random.uniform(-4,4)
    #upper boundary
    aU = np.random.uniform(0.4,1.6)
    #bias
    beta = 0.5
    #time resolution
    h = 0.001
    #number of trials
    n = 100
    #trial variability of the drift rate
    eta = np.random.uniform(0,2)
    #number of steps
    maxiter = 1000
    # decision time t
    t = np.random.uniform(0.0,0.4)
    #return random parameters
    return beta,v,eta,aU,s,h,n,maxiter,t

# generate the data we want using a set of defined parameters, take out the Nans
rt = [] #response times array
subj_idx = [] #subject number array
aU_values  = [] #true values of upper boundary aU
v_values = [] #true values of drift rate
t_values = [] #decision time
for i in range(30):
    beta,v,eta,aU,s,h,n,maxiter,t = random_parameter()
    dataEta = np.array(stoneEta(beta,v,eta,aU,s,h,n,maxiter))
    aU_values.append(aU)
    v_values.append(v)
    dataEta = dataEta[~np.isnan(dataEta)]
    t_values.append(t)
    updated_rt = []
    for k in dataEta:
        if (k >= 0):
            value = k+t
            updated_rt.append(value)
        if (k < 0):
            value = k-t
            updated_rt.append(value)
    data = np.array(updated_rt)
    rt = np.concatenate((rt,dataEta),axis=None)
    #now add a subject number column
    for j in range(len(dataEta)):
        subj_idx.append(i)
#take out all the Nans
rt = rt[~np.isnan(rt)]
# create an array for the response (1 for positive and 0 for negative)
response = []
for i in rt:
    if (i > 0 ):
        response.append(1)
    elif (i < 0):
        response.append(0)
response = np.array(response)
# since we have the response data, we use the absolute value for the rts
for i in range(len(rt)):
    rt[i] = abs(rt[i])

#put the array into a csv file
f = open('dataEta.csv', 'wb')
out = csv.writer(f, delimiter=',')
out.writerow(["subj_idx","rt","response"])
for i in range(len(rt)):
    list = [subj_idx[i],rt[i],response[i]]
    out.writerows([list])
f.close()

# load the data from the data.csv file into a variable data_stone
data_stoneEta = hddm.load_csv('dataEta.csv')

# flips the signs back
data_stoneEta = hddm.utils.flip_errors(data_stoneEta)

# Instantiate model object passing it data_stone
# This will tailor an individual hierarchical DDM around the dataset.
m = hddm.HDDM(data_stoneEta, include=('sv'))

# find a good starting point which helps with convergence
starting_values = m.find_starting_values()

# start drawing 7000 samples and discarding 5000 as burn-in
m.sample(2000, burn=20)

# Now we have an estimated model. We are going to print a summary stats table for each parameters' posterior.
stats = m.gen_stats()
stats[stats.index.isin(['a', 'a_std', 'a_subj.0', 'a_subj.1'])]

# this is used to look at is the trace, the autocorrelation, and the marginal posterior
plt.figure(6)
m.plot_posteriors(['a', 't', 'v', 'a_std'])
plt.savefig("posteriorsEta.png")

# now we want to get the ~2000 samples from the 1 chain for a,t,v (make it a pandas dataframe)
df_posteriors = pd.DataFrame(m.get_traces())

# put df_posteriors into a csv file
a = open('posteriorsEta.csv', 'wb')
out = csv.writer(a, delimiter=',')
df_posteriors.to_csv('posteriorsEta.csv', header=True, index=True)

def recovery(possamps, truevals):  # Parameter recovery plots
    """Plots true parameters versus 99% and 95% credible intervals of recovered
    parameters. Also plotted are the median and mean of the posterior
    distributions
    Parameters
    ----------
    possamps : ndarray of posterior chains where the last dimension is the
    number of chains, the second to last dimension is the number of samples in
    each chain, all other dimensions must match the dimensions of truevals
    truevals : ndarray of true parameter values
    """

    # Number of chains
    nchains = possamps.shape[-1]
    print(nchains)
    # Number of samples per chain
    nsamps = possamps.shape[-2]

    # Number of variables to plot
    nvars = np.prod(possamps.shape[0:-2])

    # Reshape data
    alldata = np.reshape(possamps, (nvars, nchains, nsamps))
    alldata = np.reshape(alldata, (nvars, nchains * nsamps))
    truevals = np.reshape(truevals, (nvars))

    # Plot properties
    LineWidths = np.array([2, 5])
    teal = np.array([0, .7, .7])
    blue = np.array([0, 0, 1])
    orange = np.array([1, .3, 0])
    Colors = [teal, blue]

    for v in range(0, nvars):
        # Compute percentiles
        bounds = scipy_stats.scoreatpercentile(alldata[v, :], (.5, 2.5, 97.5, 99.5))
        for b in range(0, 2):
            # Plot credible intervals
            plt.figure(b)
            credint = np.ones(100) * truevals[v]
            y = np.linspace(bounds[b], bounds[-1 - b], 100)
            lines = plt.plot(credint, y)
            plt.setp(lines, color=Colors[b], linewidth=LineWidths[b])
            if b == 1:
                # Mark median
                mmedian = plt.plot(truevals[v], np.median(alldata[v, :]), 'o')
                plt.setp(mmedian, markersize=10, color=[0., 0., 0.])
                # Mark mean
                mmean = plt.plot(truevals[v], np.mean(alldata[v, :]), '*')
                plt.setp(mmean, markersize=10, color=teal)
    # Plot line y = x
    tempx = np.linspace(np.min(truevals), np.max(truevals), num=100)
    recoverline = plt.plot(tempx, tempx)
    plt.setp(recoverline, linewidth=3, color=orange)

# now we want to make a 3 dimensional matrix to input to postamps posteriors.csv (for aU)
posteriors_dataEta = hddm.load_csv('posteriorsEta.csv')
a_postamps = pd.DataFrame([posteriors_dataEta['a_subj.0'],posteriors_dataEta['a_subj.1']])

for i in range(2, 30):
    col_name = posteriors_dataEta.columns[i]
    addition = pd.DataFrame([posteriors_dataEta['a_subj.%d' % (i)]])
    a_postamps = pd.concat([a_postamps,addition])
a_postamps = np.expand_dims(a_postamps, axis=1)
plt.figure(7)
recovery (a_postamps,aU_values)
plt.savefig("a_postampsEta.png")

# now we want to make a 3 dimensional matrix to input to postamps posteriors.csv (for v)
posteriors_dataEta = hddm.load_csv('posteriorsEta.csv')
v_postamps = pd.DataFrame([posteriors_dataEta['v_subj.0'],posteriors_dataEta['v_subj.1']])
for i in range(2, 30):
    col_name = posteriors_dataEta.columns[i]
    addition = pd.DataFrame([posteriors_dataEta['v_subj.%d' % (i)]])
    v_postamps = pd.concat([v_postamps,addition])
v_postamps = np.expand_dims(v_postamps, axis=1)
plt.figure(8)
recovery (v_postamps,v_values)
plt.savefig("v_postampsEta.png")

# now we want to make a 3 dimensional matrix to input to postamps posteriors.csv (for t)
posteriors_dataEta = hddm.load_csv('posteriorsEta.csv')
t_postamps = pd.DataFrame([posteriors_dataEta['t_subj.0'],posteriors_dataEta['t_subj.1']])
for i in range(2, 30):
    col_name = posteriors_dataEta.columns[i]
    addition = pd.DataFrame([posteriors_dataEta['t_subj.%d' % (i)]])
    t_postamps = pd.concat([t_postamps,addition])
t_postamps = np.expand_dims(t_postamps, axis=1)
plt.figure(9)
recovery (t_postamps,t_values)
plt.savefig("t_postampsEta.png")
