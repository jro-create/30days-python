# Day 8: Advance Data Structures in Python

# - Creating and modifying lists 
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits.remove("banana")
print("Fruits:", fruits)

# - List slicing 
print("First two fruits:", fruits[:2])

# - Creating tuples 
dimensions = (1920, 1080)
print("Screen resolution:", dimensions)

# - Accessing tuple elements 
print("Width:", dimensions[0])

# - Sets automatically remove duplicates
numbers = {1, 2, 3, 3, 4, 4, 5}
print("Unique numbers:", numbers)

# - Set operations
evens = {2, 4, 6}
odds = {1, 3, 5}
print("Union:", evens | odds)
print("Intersection:", evens & odds)

# - Creating dictionaries
student = {
    "name": "Juan",
    "age": 26,
    "grade": "A"
}

# - Adding and updating values
student["major"] = "Computer Science"
student["age"] = 27

# - Iterating through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# - Example: dictionary of lists
library = {
    "fiction": ["1984", "Dune", "Brave New World"],
    "non_fiction": ["Sapiens", "Educated"]
}

print("Fiction books:", library["fiction"])



