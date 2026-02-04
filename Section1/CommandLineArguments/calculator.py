import sys   # sys provide system spacific parameters and functions. so for cli input we need ti use this module

# Write function for add, sub and multiplication

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == 'add':
    output = add(num1, num2)
    print(output)
elif operator == 'sub':
    output = sub(num1, num2)
    print(output)
elif operator == 'multi':
    output = multi(num1, num2)
    print(output)
else: 
    print("Please give the correct operation, it is add, sub and multi")