#Day-02/examples/01-string-strip.py
#1. .strip() — The Trimmer
#The strip() method removes characters (usually whitespace) from the start and the end of a string. It does not affect the middle of the string.
#Primary Use: Cleaning up messy user input or removing trailing newline characters (\n).
text = "  Some spaces around  "
text1 = "  Python is fun  "
stripped_text = text.strip()
print("Stripped text:", stripped_text)
print(text1.strip()) 
# Output: "Python is fun" (Middle spaces stay!)