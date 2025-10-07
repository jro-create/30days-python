# Day 7 - Student Grade Analyzer (v2.0)
# This program stores multiple students' grades and calculates their averages.

students = {}

print("=== Student Grade Analyzer ===")
print("Type 'done' when finished adding students.\n")

while True:
    name = input("Enter student name: ").strip()
    if name.lower() == 'done':
        break

    grades = input(f"Enter {name}'s grades separated by spaces: ").split()
    grades = [float(g) for g in grades]  # convert all to numbers
    students[name] = grades

print("\n=== Class Summary ===")
for student, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{student}: Grades = {grades}, Average = {avg:.2f}")

# Find top student
top_student = max(students, key=lambda x: sum(students[x]) / len(students[x]))
print(f"\n🏆 Top Student: {top_student} with average {sum(students[top_student]) / len(students[top_student]):.2f}")

