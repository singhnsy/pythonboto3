# While Python has a built-in max() function, 
# here is how you would write the logic manually using a loop to compare each integer.

def find_max(numbers):
    if not numbers:     # check if the list is empty
        return None
    
    # Assume the first number is the largest to start
    max_val = numbers[0]

    for num in numbers:
        if num > max_val:
            max_val = num

    return max_val

# Example 
my_list = [23, 89, 7, 50, 80]
print(f"Largest Number: {find_max(my_list)}")


#Task: Write a function that takes a list of integers and returns the maximum value from that 
#list using the max() function.

#def max_value(numbers):
#return max(numbers)

