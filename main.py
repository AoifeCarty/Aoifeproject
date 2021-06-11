import pandas as pd
data=pd.read_csv("netflix_titles.csv")

updatedfile=data.fillna(data.mean())
print(data.shape,updatedfile.shape)



