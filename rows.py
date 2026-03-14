# datar raws dekhar jnno use kora hoe (2 types)
# #head() -> 5 raw dekhhai dibe tail()->botton er raw dekhabe


import pandas as pd



df = pd.read_csv("sales_data_sample.csv" ,encoding="latin1")
# first top theke rows dekhabe
print('Display 10 rows of first')
print(df.head(10))
# botton theke rows dekhabe
print('Display 10 rows of last')
print(df.tail(10))

print(df.columns)  # column names

print(df.info()) # column name,datatype,missing value show korbe


print(df.describe()) #mean,max,min, standard deviation count kore dibe

df.isnull().sum() # check korbe missing value ache kina

df.fillna(0) #fill kore dibe missing value into 0