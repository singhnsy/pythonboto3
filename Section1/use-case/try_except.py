import sys
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    div = a / b
    print(div)

except ZeroDivisionError:
    print("Error: Divison by Zero is not allowed")