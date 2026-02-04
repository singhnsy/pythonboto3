#Function for Addition
def add(a, b):
    return a + b
#Function for Subestraction
def sub(a, b):
    return a - b
#Function for Multiplication
def multiply(a, b):
    return a * b 
#Function for Division
def divide(a, b):
    return a / b
# Input valuea
a = 10
b = 5
# calling the funciton and print the results
print(f"Addition: {a} + {b} = {add(a, b)}") # Here f is fstring which is use to print variable value inside double quotes.
print(f"Subestraction: {a} - {b} = {sub(a,b)}")
print(f"Multiply: {a} * {b} = {multiply(a,b)}")
print(f"Dividid: {a} / {b} = {divide(a,b)}")