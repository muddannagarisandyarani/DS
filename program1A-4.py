import pandas as pd
# Creating a dictionary of student data
student_data = {
    "Roll_No": [101, 102, 103, 104],
    "Name": ["Anusha", "Babitha", "Charitha", "Deepika"],
    "Dept": ["IT", "IT", "CSE", "ECE"],
    "Percentage": [89, 92, 88, 85]
}
# Creating a DataFrame
df = pd.DataFrame(student_data)
# Displaying the DataFrame
print("Student Data:")
print(df)
# Writing data into a tab-delimited text file
df.to_csv("student_output.txt", sep="\t", index=False)
print("Data successfully written to student_output.txt")