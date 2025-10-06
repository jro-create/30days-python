# Day 7 - File Handling in Python
# Learning Notes and Examples

# --- Writing to a File ---
with open("sample.txt", "w") as file:
    file.write("This is my first file write in Python!\n")
    file.write("Python makes file handling simple.\n")
    file.write("Today I Learned about file handling inn Python.\n")

# --- Reading a File ---
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# --- Appending to a File ---
with open("sample.txt", "a") as file:
    file.write("Appending another line!\n")

# --- Reading Line by Line ---
with open("sample.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

