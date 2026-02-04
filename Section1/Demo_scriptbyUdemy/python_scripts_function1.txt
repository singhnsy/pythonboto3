def shikhar():
    print("Hello, World!")
# calling the function
shikhar()

===============
===============

#Function with Parameters
def greet(name, age):
    print(f"Hello, {name} ! you are {age} years old.")

# calling the function with arguments

greet("Shikhar", 35)

=========
=========

# Function with Return Value
def add(a, b):
    return a + b

# Calling the function and storing the result
result = add(10, 12)
print (f"The sum is: {result}")

==========
==========

# Function for Addition
def add(a, b):
    return a + b

#Function for Subtraction
def subtraction(a, b):
    return a -b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division
def divide(a, b):
    return a / b

# Input Values
a = 10
b = 5

# Calling the functions and print the results
print(f"Addition: {a} + {b} = {add(a, b)}")
print(f"Subtraction: {a} - {b} = {subtraction(a, b)}")
print(f"Multiplication: {a} * {b} = {multiply(a, b)}")

=========
=========

# Here’s a Python script for addition, subtraction, multiplication, and division without using functions:

# Addition
x = 10
y = 5
addition = x + y
print(f"Addition: {x} + {y} = {addition}")

# Subtraction
subtraction = x - y
print(f"Subtraction: {x} - {y} = {subtraction}")

# Multiplication
multiplication = x * y
print(f"Multiplication: {x} * {y} = {multiplication}")

# Division
division = x / y
print(f"Division: {x} / {y} = {division}")

============
============

# Here’s the same script, but this time using functions to perform each operation:

# Function for Addition
def add(a, b):
    return a + b

# Function for Subtraction
def subtract(a, b):
    return a - b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division
def divide(a, b):
    return a / b

# Input values
x = 10
y = 5

# Call the functions and print the results
print(f"Addition: {x} + {y} = {add(x, y)}")
print(f"Subtraction: {x} - {y} = {subtract(x, y)}")
print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
print(f"Division: {x} / {y} = {divide(x, y)}")

=============
=============

