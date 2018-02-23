import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
 
# 加载数据
# 备用地址: http://cdn.powerxing.com/files/lr-binary.csv
df = pd.read_csv("lr-binary.csv")
 
# 浏览数据集
print(df.head())
#    admit  gre   gpa  rank
# 0      0  380  3.61     3
# 1      1  660  3.67     3
# 2      1  800  4.00     1
# 3      1  640  3.19     4
# 4      0  520  2.93     4
 
# 重命名'rank'列，因为dataframe中有个方法名也为'rank'
df.columns = ["admit", "gre", "gpa", "prestige"]
print(df.columns)
# array([admit, gre, gpa, prestige], dtype=object)