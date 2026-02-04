# Import the user defined module
import mymodule

# Use the functions  and variables from the modules (mymodule)
name = "Narendra"
greeting =  mymodule.greet(name)
print(greeting)

# Using the add function
result = mymodule.add(10, 20)
print(f"10 + 20 = {result}")