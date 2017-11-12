import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt 

from scipy.stats import wilcoxon
df = pd.read_csv('./dataframe.csv')

#T-test
print wilcoxon(df['mean_paired_difference'].dropna().values)
#Ttest_1sampResult(statistic=-1.7689154347000551, pvalue=0.084346926924775634)
#WilcoxonResult(statistic=104.5, pvalue=0.0082216482123530915)

#Linear Regression
result = sm.ols(formula="cbd_us ~ cbd_ct + 1", data=df).fit()
print result.summary()

#Plot linear regression
# regress "expression" onto "motifScore" (plus an intercept)
p = result.fit().params

fig = plt.figure()
ax = fig.add_subplot(111)

# scatter-plot data
ax = df.plot(x='cbd_ct', y='cbd_us', kind='scatter')

# plot regression line on the same axes, set x-axis limits
ax.plot(x, p.const + p.cbd_us * x)
ax.set_xlim([1, 2])