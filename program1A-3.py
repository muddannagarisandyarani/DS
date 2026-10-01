import pandas as pd
data = {
    "RollNo": [101, 102, 103],
    "Name": ["Rahul", "Priya", "Akhil"],
    "Marks": [85, 92, 78]
}
df = pd.DataFrame(data)
print(df)