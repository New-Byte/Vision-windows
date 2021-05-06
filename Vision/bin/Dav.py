import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pandas as pd

#get input
file = sys.argv[1]

#load dataset
dataset = pd.read_csv("C:\\Vision\\Vision-windows\\Vision\\data\\"+file)

#corr
mat = dataset.corr()

for x in mat:
    for y in mat:
        if mat[x][y] > 0.6 and mat[x][y] < 1:
            sns.catplot(x=x, y=y, kind="bar", data=dataset)
            plt.show()
            
#Plot Graphs
#sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker",data=data)
#sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=data)
#sns.relplot(x=x, y=y, ci=None, kind="line", data=dataset)
#sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=data)
