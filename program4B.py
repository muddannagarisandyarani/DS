import pandas as pd
index = pd.MultiIndex.from_tuples(
    [
        ('Computer', 'Java'),
        ('Computer', 'Python'),
        ('Mathematics', 'Algebra'),
        ('Mathematics', 'Calculus')
    ],
    names=['Department', 'Subject']
)
data = pd.DataFrame(
    {
        '2025': [75, 82, 90, 86],
        '2026': [80, 88, 92, 89]
    },
    index=index
)
print("Original Tabular Data:")
print(data)
unstacked_data = data.unstack()
print("\nData after Unstack():")
print(unstacked_data)
stacked_data = unstacked_data.stack()
print("\nData after Stack():")
print(stacked_data)