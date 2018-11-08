# implemnt the loop for the approximation of pi
n = 0
pi = 0

while(n < 10000):
    pi += ((-1) ** n * 4) / (2 * n + 1)
    n += 1

print(pi)
# output: 3.1414926535900345