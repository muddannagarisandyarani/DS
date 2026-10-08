import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print(df.head())
print(df.describe())
print(df.groupby('species')['sepal_length'].agg(
    ['count','sum','mean','std','min','max']
))
print(df.groupby(['species','sepal_width'])['sepal_length'].mean())
print(df.groupby('species').agg({
    'sepal_length':['mean','std','min','max'],
    'sepal_width':['mean','std','min','max'],
    'petal_length':['mean','std','min','max'],
    'petal_width':['mean','std','min','max']
}))
print(df['species'].value_counts())
print(df.groupby('species')['petal_length'].mean())
print(df.groupby('species')['petal_width'].mean())
print(df.groupby('species')['sepal_length'].max())