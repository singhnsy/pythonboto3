#s4.py
#=====

age = 32

# The test condition is always True
while age > 18:
    print(f'You can vote : {age}')
    age = age - 1         ## if we remove this, then it will run infinite time..
