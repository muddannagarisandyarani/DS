import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
df.to_csv("iris_output.csv", index=False)
print("The dataset has been successfully written to iris_output.csv")