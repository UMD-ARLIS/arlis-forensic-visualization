
import pandas as pd 
import matplotlib.pyplot as plt 

# How many types of harm have moderate and above sevirity 
harm_df = pd.read_csv('harm_sheet_2022-06-06.csv')
crit_df = harm_df[(harm_df['classifications.Severity'].isin(["Moderate",
            "Severe","Critical"]))][['classifications.Severity',
            'classifications.Harm Type']]
      
                                                                            

#Structure of list is Type of harm, Moderate, Severe, Critical
all_data_df = pd.DataFrame([['Physical Health/Safety',1,6,1],
            ['Physical Property',1,1,1],
            ['Psychological',4,0,1],
            ['Intangible Property',0,0,1],
            ['Civil Liberties',7,0,0],
            ['Financial',2,1,0],
            ['Social or Political Systems',2,0,0]],
            columns=['Type of Harm','Moderate','Severe','Critical'])
print(all_data_df)


# STACKED BAR GRAPH
all_data_df.plot(x='Type of Harm', kind='bar', stacked=True, 
                 title='Types of Harm by Severity (Moderate and Above)',)
plt.ylabel("Number of AI Incidients")
plt.xticks(rotation='horizontal')
plt.show()



