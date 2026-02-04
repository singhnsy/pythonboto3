# 1 Ask user for input
# We wrap input() in float() to handle decimals like 85.5.
try:
    score = float(input("Enter your score (0-100): "))

    # 2 Determine the grade using if-elif-else login
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    elif score < 60 and score >=0:
        grade = 'F'
    else:
        grade = "Invalid (Score must be between 0 to 100)"

    # 3 Output result
    print(f"your grade is: {grade}")

except:
    print("Error: Please enter a valid numerical number")
