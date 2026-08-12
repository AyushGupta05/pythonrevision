import pandas as pd 

# 2d data 

data = {"Name":["ayush", "aavya", "aarav"], 
        "Age" : [18,19,14] }

df = pd.DataFrame(data, index = [1,2,3])

#print(df.loc[1])

# add a new column
df["Job"] = ["student math", "student physics", "studebntig"]

# adding a new row 
new_row = pd.DataFrame([{"Name": "Abhinav", "Age" : 28, "Job" : "banker"}], index = ["Employee 4"])

df = pd.concat([df,new_row])


print(df)