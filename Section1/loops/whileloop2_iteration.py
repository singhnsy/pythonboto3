#In Python, iteration is the process of executing a block of code repeatedly over a sequence 
# (like a list, string, or range). It is one of the most powerful tools in a developer's kit 
# because it allows you to automate repetitive tasks with just a few lines of code.

i = 0
while True:
    print(f"Iteration: {i}")
    i += 1
    # Break the loop when i reaches 5
    if i == 9:
        print("Breaking the loop.")
        break

print("Loop has been terminated.")
