###simple Call##
def add (a, b):
    print(a + b)
## Calling the function
add(5,6)


### Return the value ###
def add1(c, d):
    return c + d
result = add1(5, 30)
print(result)

## Return multiple value
def get_details():
    name = "Raja"
    age = 20
    department =  "CS"
    return name, age, department
details = get_details()
print(details)

