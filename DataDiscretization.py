import pandas as pd

df = pd.DataFrame({'Age': [15, 22, 35, 42, 51, 63, 75]})

# Define bins correctly
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 18, 40, 60, 100], labels=['Teens', 'Young adult', 'Middle-aged', 'Senior'])

# Define the hierarchy mapping
hierarchy = {
    'Teens': 'Young',
    'Young adult': 'Young',
    'Middle-aged': 'Adult',
    'Senior': 'Elder'
}

# Apply the mapping to create a new column with hierarchy values
df['Hierarchy'] = df['AgeGroup'].map(hierarchy)

print(df)
