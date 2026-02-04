## Dictionary data type : unordered collection and mutable 
employee = {
    "name":"John Dev",
    "age":30,
    "position":"software engineer",
    "salary":80000
}
print(employee["name"])
print("Employee details:",employee)

## mutable
employee["department"]="IT"
print("Employee details:",employee)

## change key value 
employee["salary"] = 85000
print("Employee details:",employee)