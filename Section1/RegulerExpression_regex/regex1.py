import re    # Here re is a module (powerfull toll)
### re.match() #### 
text = "hello word"
pattern = r"hello"
result = re.match(pattern, text)      ## determine if the regex matches at the begnning of the string.
print (result)

### re.search() #### 
text1 = "Hi this is Narendra singh From Noida and Narendra From Agra as well"
pattern1 = r"Narendra"
result1 = re.search(pattern1, text1)   ## Search the string for a matche and returen the first occuronce.
print(result1)

if result1:
     print(result1.group())

### re.findall() #### 
text2 = "Hi this is vanya \
    and to learn python \
        whihc is helpfiul in my python project"
pattern2 = r"python"
result2 = re.findall(pattern2, text2)  ##Returns a list for all matches in the string.
print(result2)

### re.sub() #### 
pattern3 =  r"\s+"   ## One or more spaces
string =  "Python    is      great"    ## here we can see multiple whitespace, it mean sentens is not writter proper way.
print(string)
new_string =  re.sub(pattern3," ", string)  ### Replace matches (remove unused whilespace and keep only require) with a new string.
print(new_string) 