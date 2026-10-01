import pandas as pd
df = pd.DataFrame({
    'gender': ['male', 'female', 'male']
})
df['gender_num'] = df['gender'].map({
    'male': 0,
    'female': 1
})
df_renamed = df.rename(columns={'gender': 'Gender'})
print(df_renamed)