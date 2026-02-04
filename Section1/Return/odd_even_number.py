def check_even(number):
    if number % 2 == 0:   # % (Modulo Operator): This calculates the remainder of a division.
        return "Even"
    return "Odd"

result = check_even(87)     ### change with odd and even numbers
print(result)