#A palindrome is a word that reads the same backward as forward. 
#We use Python's slicing feature [::-1] to reverse the string and compare it to the original.

def is_palindrom(text):
    #Convert to lowercase to ensure the check is case-insenstive
    clean_text = text.lower()
    #Compare the string with its reverse
    return clean_text == clean_text[::-1]

#Example Usage 
print(is_palindrom("Radar"))   ## Output : True
print(is_palindrom("Python"))  ## Output : False