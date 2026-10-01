import pandas as pd
excel_data = pd.read_excel(
    "College-data.xlsx",
    sheet_name=None
)
print(excel_data.keys())
print("In Student sheet:")
print(excel_data["Students"])
print("In Course sheet:")
print(excel_data["Courses"])