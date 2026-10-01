import requests
import pandas as pd
url = "https://api.github.com/repos/pandas-dev/pandas/issues"
response = requests.get(url)
issues = response.json()
df_issues = pd.DataFrame(issues)
print(df_issues[["id", "title", "state", "created_at"]].head(30))