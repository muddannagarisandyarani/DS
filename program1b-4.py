import pandas as pd
url = "https://jsonplaceholder.typicode.com/users"
df = pd.read_json(url)
print(df.head())