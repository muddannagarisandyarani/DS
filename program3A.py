import numpy as np
import pandas as pd
data = {'A': [1, 2, np.nan],
        'B': [4, np.nan, np.nan]}
df = pd.DataFrame(data)
print(df.isna())
df_clean = df.dropna()
df_filled = df.fillna(0)
print(df_clean)
print(df_filled)
df = df.drop_duplicates()