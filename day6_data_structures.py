# Day 6: Python Data Structures
# -----------------------------
# Today we learn about Lists, Tuples,  Sets, and  Dictionaries.

# These are the core ways Python organizes and stores collections of data.

# --- LISTS ---
# Ordered, changeable, allow duplicates
print("\n--- LISTS ---")
movies = ["Akira", "Blade Runner", "Speed Racer", "Mission Impossible 7", "Spirited Away"]
print("My favorite movies:", movies)
print("Third movie:", movies[2])
movies.append("Parasite")
print("After adding one:", movies)

# --- Tuples ---
# Ordered, but  unchangeable, allow duplicates
print("\n--- TUPLES ---")
birth_info = (11, 1996)
print("Birth month:", birth_info[0])
print("Birth year:", birth_info[1])

# --- SETS ---
# Unordered, no duplicates.
print("\n--- SETS ---")
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Original list with duplicates:", numbers)
print("After converting to set (no duplicates):", unique_numbers)

# --- DICTIONARIES ---
# Key-value pairs
print("\n--- DICTIONARIES ---")
student = {"name": "Thalia", "age": 29, "city": "San Juan"}
print("Student dictionary:", student)
print("Student name:", student["name"])
print("Student age:", student["age"])
print("Student city:", student["city"])

