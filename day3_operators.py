# day3_operators.py
# Day 3: Operators & Expressions

# Arithmetic operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (Remainder):", a % b)
print("Exponentiation:", a ** b)

# Comparison operators
print("Is a equal to b?", a == b)
print("Is a not equal to b?", a != b)
print("Is a greater than b?", a > b)
print("Is a less or equal to b?", a <= b)

# Logical operators
print("True and False:", True and False)
print("True or False:", True or False)
print("Not True:", not True)

# Assignment operators
x = 5
x += 2 # x = x + 2
print("x after += 2:", x)
x *= 3 # x = x * 3
print("x after *= 3:", x)

# Combined expressions
result = (5 + 3) * 2 ** 2 // 4
print("Combined expression result:", result)

# Challenge: Even or odd check
n = 15
print("Is n even", n % 2 == 0)

# Challenge: Check if number is between 10 and 20
print("Is n between 10 and 20?", n > 10 and n < 20)
