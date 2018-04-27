import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import numpy as np 

from pprint import pprint
from matplotlib import rcParams
from statsmodels.sandbox.regression.predstd import wls_prediction_std

rcParams['text.usetex'] = True 

filename = "./CBD-US, CT Discrepancy.xlsx"

df = pd.read_excel(filename, sheetname="Sheet1")

#Format Data

df['mean_paired_difference'] = df['cbd_us'] - df['cbd_ct']
df['average'] = 0.5*(df['cbd_us']+df['cbd_ct'])

#Bland-Altman plot is PCA of variables, i.e. (mean, diffference)
fig = plt.figure()
ax = fig.add_subplot(111)

rlm_model = sm.RLM(df['mean_paired_difference'],sm.add_constant(df['average']), M=sm.robust.norms.HuberT(), missing='drop')
rlm_results = rlm_model.fit()

g = sns.regplot(x='average',y='mean_paired_difference', data=df, ax=ax, truncate=True, robust=True)
sns.despine(offset=10, trim=True)

ax.axhline(y=0,color='k',linestyle='--')
ax.axhline(y=0+df['average'].mad(),color='k',linestyle='--')
ax.axhline(y=0-df['average'].mad(),color='k',linestyle='--')

ax.set_xlabel(r'$\frac{1}{2} \cdot \left( \textrm{US + CT}\right) \left(mm\right)$')
ax.set_ylabel(r'$\textrm{US - CT }\left(mm\right)$')
ax.set_aspect('equal')

m = (1-0.5*rlm_results.params['average'])/(1+0.5*rlm_results.params['average'])
b = rlm_results.params['const']/(1-0.5*rlm_results.params['average'])
plt.text(20, 10, r'$\textrm{CT}=%.02f\cdot \textrm{US} %.02f$'%(m,b), fontsize=12)
plt.tight_layout()
plt.savefig('bland-altman.png',dpi=400)
