#Import the package (my_package)
import my_package

#Use functions from the package

result_add = my_package.add(5, 4)
result_sub = my_package.subtract(4, 2)
result_upper = my_package.to_upper("hello")
result_lower = my_package.to_lower("Narendra")


print(f"Addition : {result_add}")
print(f"Subestraction: {result_sub}")
print(f"Upeer case: {result_upper}")
print(f"Lower case: {result_lower}")