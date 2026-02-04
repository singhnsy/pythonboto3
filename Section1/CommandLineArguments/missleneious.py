import sys   # sys provide system spacific parameters and functions. so for cli input we need ti use this module

# Print all command-line arguments
print("Arguments passed:", sys.argv)

# First argument is always the script name
script_name = sys.argv[0]
print("Script name:", script_name)

# Other arguments are passed from index 1 onward
if len(sys.argv) > 1:
    first_argument = sys.argv[1]
    print("First argument:", first_argument)
else:
    print("No arguments passed.")