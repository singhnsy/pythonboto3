#1# Fucntion without parameters
def narendra():
    print("Hello, Veenu")
#calling the funcion wihtout agrument
narendra()


#2# Fucntion with parameters
def greet(name, age):
    print (f"Hello, {name} ! you are {age} years old !")   #Here f is fstring which is use to print variable value inside double quotes.

# calling  the funcitn with arguments
greet("Raj", 30)

#3# Function with return value
def add(a, b):
    return a * b   ## here reture value to function and store into result variable as below.    

# calling the function and storing the result
result = add(10,12)
print(f"The sum is the {result}")  # Here f is fstring which is use to print variable value inside double quotes.




