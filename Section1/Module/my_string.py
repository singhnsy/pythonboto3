# Task: Write a script that converts a string to uppercase and checks if it contains a specific substring.
# While Python’s str class handles most of this, the string module is great for accessing predefined character sets. 
# Here is the script for your task.

import string

# 1 Define the input string
raw_data = "devsecops_pipeline_v1_stable"

# 2 Convert to upper case
# Note: .upper() is a method built into every string object
shouting_data = raw_data.upper()

# 3 Define the substring to search for 
search_term = "PIPELINE"

# 4 Check the substring present 
# The 'in' keyword is the pythonic way to check for membership
exists = search_term in shouting_data

##---Output---
print(f"Original: {raw_data}")
print(f"Uppercase: {shouting_data}")

if exists:
    print(f"Success: '{search_term}' was found in the string")
else:
    print(f"Error: '{search_term}' not found")

# Bonus: Using the string module to check for punctuation, digits and ascii_letters
print(f"Standard Punctuation: {string.punctuation}")
print(f"Standard digites: {string.digits}")
print(f"Standard ascii_letters: {string.ascii_letters}")

# Output Result:
# Original: devsecops_pipeline_v1_stable
# Uppercase: DEVSECOPS_PIPELINE_V1_STABLE
# Success: 'PIPELINE' was found in the string
# Standard Punctuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# Standard digites: 0123456789
# Standard ascii_letters: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ