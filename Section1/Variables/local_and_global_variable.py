##### Local Variables
def my_function():
    print("Hello from a function and local variable")
my_function()

def addition():
    num1 = 20
    num2 = 10
    print(num1 + num2)
addition()

def subestraction():
    num1 = 20
    num2 = 10
    print(num1 - num2)
subestraction()

### Global Variables
num1 = 40
num2 = 30
def my_function():
    print("Hello from a function and global variables")
my_function()

def addition():          ### here this function will pic value from locally. if not in function then gloablly.
    num1 = 20 
    num2 = 10
    print(num1 + num2)
addition()

def subestraction():
    print(num1 - num2)
subestraction()
