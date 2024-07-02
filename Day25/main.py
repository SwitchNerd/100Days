import time 
import pandas

f = pandas.read_csv('Day25\weather_data.csv')
monday = f[f.day == 'Monday']
temp = monday.temp

temp = (temp *(9/5)) + 32
print(temp)

#To convert to data frame 
# pandas.Dataframe(*dictionary*)