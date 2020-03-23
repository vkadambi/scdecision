import seaborn as sns
import csv
import hddm
import scipy.io as sio
from scipy import stats
from IPython import get_ipython  # Run magic functions from script
get_ipython().magic('pylab')  # Initialize ipython matplotlib plotting graphics

from recovery import recovery

#first define the stone function
def stone (beta,v,aU,s,h,n,maxiter) :
    return beta,v,aU,s,h,n,maxiter

# generate the data we want using a set of defined parameters, take out the Nans
rt = [] #response times array
subj_idx = [] #subject number array
aU_values  = [] #true values of upper boundary aU
v_values = [] #true values of drift rate
for i in range(30):
    beta,v,aU,s,h,n,maxiter = random_parameter()
    data = np.array(stone(beta,v,aU,s,h,n,maxiter))
    aU_values.append(aU)
    v_values.append(v)
    data = data[~np.isnan(data)]
    rt = np.concatenate((rt,data),axis=None)
    #now add a subject number column
f.close()

#plot for fun
plt.figure(5)
sns.distplot(data[~np.isnan(data)], hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('HDDM Graph')
plt.xlabel('Reaction Times')
out = csv.writer(a, delimiter=',')
df_posteriors.to_csv('posteriors.csv', header=True, index=True)

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
        bounds = stats.scoreatpercentile(alldata[v, :], (.5, 2.5, 97.5, 99.5))
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

#now we want to make a 3 dimensional matrix to input to postamps posteriors.csv (for aU)
posteriors_data = hddm.load_csv('posteriors.csv')
a_postamps = pd.DataFrame([posteriors_data['a_subj.0'],posteriors_data['a_subj.1']])
for i in range(5, 33):
    col_name = posteriors_data.columns[i]
    addition = pd.DataFrame([posteriors_data[col_name]])
    a_postamps = pd.concat([a_postamps,addition])
a_postamps = np.expand_dims(a_postamps, axis=1)
recovery(a_postamps,aU_values)
