import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

"""
There is a lot going on here with a few unfinished ideas. 

Every idea is attempting to tackle the same concept of graphing location
by harm basis, and each idea is grouped by triple quotes and titles

so far only the horizontal bar graph is fully working, so I copyed that 
out of the quotes so something runs right off of the bat"""

#DATA READING
df = pd.read_csv('harm_basis_by_location_2022-06-06.csv')

#Grouped Horizontal Bar Graph
sns.countplot(y="Harm Distribution Basis", hue='Location', data=df)



"""
#Grouped Horizontal Bar Graph
# WHAT LOCATIONS HAVE THE DIFFERNT HARMS ASSOCIATED WITH THEM
#sns.countplot(y="Location", hue='Harm Distribution Basis', data=df)

# FLIP X and Y 
sns.countplot(y="Harm Distribution Basis", hue='Location', data=df)
"""


"""
#STRIP PLOT
sns.stripplot(x='Location', y='Harm Distribution Basis', data = df, 
              jitter = True, hue = 'Near Miss', dodge = True,)
plt.ylabel("Harm Basis Types")
title='Harm Basis per Location by Harm Caused'
plt.xticks(rotation='horizontal')

#MAKING LEGEND 
print(df["Near Miss"].value_counts)
hc= (df['Near Miss'] == 'Harm caused').value_counts
nm = (df['Near Miss'] == 'Near miss').value_counts
uu = (df['Near Miss'] == 'Unclear/unknown').value_counts
plt.legend(labels=[f"Harm Caused({hc})",f"Near Miss({nm})", f"Unclear/unknown({uu})"])
"""



"""
#VIOLIN PLOT WITH COLORED SWARMPLOT INSIDE FOR NEAR MISS
g = sns.catplot(x="Location", y="Harm Distribution Basis", kind="violin", inner=None, data=df)
sns.swarmplot(x="Location", y="Harm Distribution Basis", color="k", size=3, data=df, ax=g.ax)
#need to adjust for non-numeric variables
"""

plt.show()