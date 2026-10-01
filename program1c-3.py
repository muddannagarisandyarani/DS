import pandas as pd
student_data = {
    "Roll No": [101, 102, 103],
    "Name": ["Anusha", "Babitha", "Charitha"],
    "Department": ["IT", "IT", "CSE"],
    "Percentage": [89, 92, 88]
}
course_data = {
    "Course ID": ["C101", "C102", "C103"],
    "Course Name": ["Python", "Data Science", "Machine Learning"],
    "Credits": [4, 3, 4]
}
students_df = pd.DataFrame(student_data)
courses_df = pd.DataFrame(course_data)
with pd.ExcelWriter("College-data.xlsx", engine="openpyxl") as writer:
    students_df.to_excel(writer, sheet_name="Students", index=False)
    courses_df.to_excel(writer, sheet_name="Courses", index=False)
print("Multiple sheets successfully written to College-data.xlsx")