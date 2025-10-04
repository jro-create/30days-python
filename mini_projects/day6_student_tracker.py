# Day 6: Student Tracker Mini-Project (Using Dictionaries)

# Global dictionary to hold student data (ID is the key)
student_records = {}

def add_student(student_id, name, grade):
    """Adds a new student to the records."""
    if student_id not in student_records:
        student_records[student_id] = {
            "name": name,
            "grade": grade
        }
        print(f"✅ Student {name} added successfully.")
    else:
        print(f"❌ Error: Student ID {student_id} already exists.")

def display_all_students():
    """Prints all student records."""
    if not student_records:
        print("📋 The tracker is currently empty.")
        return

    print("\n--- Student Records ---")
    for student_id, data in student_records.items():
        print(f"ID: {student_id} | Name: {data['name']} | Grade: {data['grade']}")
    print("------------------------")

# --- Example Usage ---
add_student("S101", "Alice Johnson", "A")
add_student("S102", "Bob Williams", "B+")
display_all_students()
