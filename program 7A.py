import pandas as pd
data = {
    'Name':['Ravi','Sita','Arun','Priya','Kiran','Anil','Lakshmi','Rahul'],
    'Department':['CSE','CSE','ECE','ECE','CSE','ECE','CSE','ECE'],
    'Year':[2,2,3,3,2,3,3,2],
    'Marks':[85,90,78,88,75,82,95,70]
}
df = pd.DataFrame(data)
print(df.groupby('Department')['Marks'].mean())
print(df.groupby(['Department','Year'])['Marks'].mean())