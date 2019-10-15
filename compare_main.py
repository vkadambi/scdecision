import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
from compare_function import stone
from micheal_code import simuldiffn200

#Stone function call
data_stone = stone(0.5,1,1,1,0.001,100,1000)
data_stone = np.array(data_stone)
# simuldiffn200 function call
data_mic = simuldiffn200(100,1,.2,.2,1,None,0,0,0,.3,1)
data_mic = np.array(data_mic)
#Stone plot
sns.distplot(data_stone[~np.isnan(data_stone)], hist=True, kde=True,bins=int(180/5), color = 'darkblue',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
sns.distplot(data_mic[~np.isnan(data_mic)], hist=True, kde=True,bins=int(180/5), color = 'purple',hist_kws={'edgecolor':'black'},kde_kws={'linewidth':4})
plt.title('Comparsion of the Two Codes')
plt.xlabel('Reaction Times')
plt.ylabel('Frequency')
plt.savefig("stone_compare.png")
