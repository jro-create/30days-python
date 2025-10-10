# ---------------------------------------
# 🧠 Day 9: Data Persistence/File Handling (Text, JSON, CSV)
# ---------------------------------------

import json
import csv

# 1️⃣ Basic Text File Read & Write
print("\n--- Working with Text Files ---")

# Write to a text file
with open("notes.txt", "w") as file:
    file.write("Today I learned about file handling in Python!\n")
    file.write("Files can store data persistently.\n")

# Read from the text file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# 2️⃣ JSON Files (Structured Data)
print("\n--- Working with JSON Files ---")

# Create a dictionary
student = {"name": "Juan", "age": 27, "courses": ["Python", "Django", "Git"]}

# Write dictionary to JSON
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Read JSON back into Python
with open("student.json", "r") as file:
    data = json.load(file)
    print("Loaded from JSON:", data)

# 3️⃣ CSV Files (Tabular Data)
print("\n--- Working with CSV Files ---")

# Write to CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Ana", 22, "Python"])
    writer.writerow(["Luis", 25, "Django"])

# Read from CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 4️⃣ Error Handling with Files
print("\n--- Error Handling ---")

try:
    with open("missing.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("⚠️ File not found. Please check the filename.")

