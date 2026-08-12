import pandas as pd

calories= {"Day1": 1750, "Day2": 1950, "Day3": 2150, "Day4": 2653, "Day5": 750, "Day6": 2023 }

series = pd.Series(calories)

#print(series) # in case of a dictionary the key becomes the label 

#print(series.loc["Day3"])

series.loc["Day3"] += 300

#print(series.loc["Day3"])

#print(series[series > 2000])

series = series[series > 2000]

