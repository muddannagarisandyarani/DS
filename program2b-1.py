import sqlite3
import pandas as pd
# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER,
    name TEXT
)
""")
# Insert data
cursor.execute("INSERT INTO Students VALUES (1, 'John')")
conn.commit()
# Read data
df = pd.read_sql_query("SELECT * FROM Students", conn)
print(df)
# Update data
cursor.execute("UPDATE Students SET name='Alice' WHERE id=1")
# Delete data
cursor.execute("DELETE FROM Students WHERE id=1")
conn.commit()
conn.close()