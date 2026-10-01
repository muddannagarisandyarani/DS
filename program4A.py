import pandas as pd
index = [
    ['Computer', 'Computer', 'Mathematics', 'Mathematics'],
    ['Java', 'Python', 'Algebra', 'Calculus']
]
multi_index = pd.MultiIndex.from_arrays(index, names=['Department', 'Subject'])
marks = pd.Series(
    [90, 85, 95, 89],
    index=multi_index
)
print("Original Series:")
print(marks)
print("\nData for Computer:")
print(marks.loc['Computer'])
print("\nData for Java:")
print(marks.loc[('Computer', 'Java')])
print("\nData for Mathematics:")
print(marks.loc['Mathematics'])