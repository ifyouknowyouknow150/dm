import pandas as pd

#Dataset one
df1 = pd.DataFrame({
    'ID': [1,2,3,4],
    'Name':['Alice','Bob',None,'David'],
    'Age': [25,None,30,22]
})

#Data set 2
df2  = pd.DataFrame({
    'ID': [3,4,5,6],
    'Salary': [50000,60000,55000,70000]
})

df1.fillna({'Name': 'Unknown', 'Age': df1['Age'].mean()},inplace=True)

#Merging two dataset
df_merged= pd.merge(df1,df2, on='ID', how = 'outer')

#Drop "Age" column from the table
df_reduced = df_merged.drop(columns=['Age'])

#Display the reslt
print(df_merged)
