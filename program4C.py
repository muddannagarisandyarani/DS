import pandas as pd
df1 = pd.DataFrame(
    {
        'Name': ['Anil', 'Priya', 'Rahul'],
        'Marks': [76, None, 84],
        'Grade': ['B', 'A', None]
    },
    index=[201, 202, 203]
)
df2 = pd.DataFrame(
    {
        'Name': ['Anil', 'Priya', 'Rahul'],
        'Marks': [89, 91, 79],
        'Grade': ['None', 'A', 'B']
    },
    index=[201, 202, 204]
)
print("First DataFrame:")
print(df1)
print("\nSecond DataFrame:")
print(df2)
merger = pd.merge(
    df1,
    df2,
    left_index=True,
    right_index=True,
    how='outer',
    suffixes=('_Df1', '_Df2')
)
print("\nMerged DataFrame:")
print(merger)
combined = df1.combine_first(df2)
print("\nDataFrame after combine_first():")
print(combined)