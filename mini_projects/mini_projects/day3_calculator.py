# day3_calculator.py
# Day 3 Mini Project: Simple Calculator

print("=== Simple Calculator ===")

# Ask the user for numbers
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

# Ask the user for the operation
operation = input("Enter operation (+, -, *, /): ")

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error ! Division by zero."
else:
     result = "Invalid operation."

# Show the result
print("Result:", result)
