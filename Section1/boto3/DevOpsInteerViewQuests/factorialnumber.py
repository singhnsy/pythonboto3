# How it Works:
# To find the factorial of a number, you simply multiply that number by every whole number below it until you reach 1.
# $3! = 3 x 2 x 1 = 6
# $5! = 5 x 4 x 3 x 2 x 1 = 120

# The Special Case: By definition, $0! = 1$. This might seem weird, but it makes mathematical formulas (like combinations and permutations) work correctly!
# The formula is expressed as:$
# $n! = n x (n-1) x (n-2) x ..... x 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(3)) 


    
    