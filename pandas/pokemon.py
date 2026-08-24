import pandas as pd 

df = pd.read_csv("pokemon.csv")


#print(df)
# its normally truncated so use to string, 

#print(df.to_string())

print(df.loc[df["legendary"] == True])
# give me the rows where this is true 

# .ffill() means use fill forwarx 
#.ffill(axis = 1) fill from left 


# or 
#for i in range(len(df)):
#    for j in range(1, len(df.columns)):
#        if pd.isna(df.iloc[i, j]):
#           df.iloc[i, j] = df.iloc[i, j - 1]

