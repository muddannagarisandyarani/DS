import pandas as pd
df = pd.read_excel(
    "Students.xlsx",
    sheet_name="Student Details"
)
print("Data read from Excel file:")
print(df)