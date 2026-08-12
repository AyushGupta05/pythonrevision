import pandas as pd


# series is a pandas 1d array that can hold any data type 

data = [1,2,100,2,2,2,43,5,6,2]
index = [i for i in range(1,len(data)+1)]
series = pd.Series(data,index = index)


#bottom has metadata, and index and normal column 

print(series.loc[3])

# print value at index i 

#series.loc[3] = 200
#print(series.loc[3])
# access it like that 


#print(series.iloc[0])
# iloc is integer location

#filtering by values

series = series [series >= 10]

print(series)