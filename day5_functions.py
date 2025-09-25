# day5_functions.py
# Learning Functions in Python

# 1. Simple Function
def greet():
    print("Hello, World!")

# 2. Function with parameter
def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

# 3. Function with return value
def square(number):
    return number * number

# 4. Function to check even/odd
def is_even(n):
    return n % 2 == 0

# 5. Factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the functions 
if __name__ == "__main__":
    greet()
    greet_user("Juan", 27)
    print("Square of 5:", square(5))
    print("Is 4 even?", is_even(4))
    print("Factorial of 5:", factorial(5))
