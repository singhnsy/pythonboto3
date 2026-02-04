import sys   # sys provide system spacific parameters and functions. so for cli input we need ti use this module

#Print all command line arguments
print("Argemtns Passed:", sys.argv)

#Print the script name command line arguments
print("Script name is", sys.argv[0])

# Other arguments are passed from index 1 onword.
if len(sys.argv) > 1 :
    first_argument = sys.argv[1] 
    print("first argument:", first_argument)
else:
    print("No Argument passed")