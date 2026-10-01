import pandas as pd
student_data = {
    "Roll_No": [101, 102, 103, 104],
    "Name": ["Anusha", "Babitha", "Charitha", "Deepika"],
    "Department": ["IT", "IT", "CSE", "ECE"],
    "Marks": [89, 92, 88, 95]
}
df = pd.DataFrame(student_data)
df.to_json(
    "students.json",
    orient="records",
    indent=4
)
print("JSON file created successfully.")