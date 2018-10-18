#Task 9b
#find the errors

# broken

# sqrt() does not work without first importing the math module 
"""
x = 2
y = 0

if 1 + x > x ** sqrt(2):
    y = y + x
"""
# the if statement needs parenthesis()

# fixed
import math

x = 2
y = 0

if (1 + x) > (x ** math.sqrt(2)):
    y = y + x

print(x ** math.sqrt(2))
