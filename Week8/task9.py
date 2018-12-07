def f(a):
    if a < 0:
        # if n is less than 0
        return -1
    n = a # assign n to a
    while n > 0:
        if n % 2 == 0: # if n is even
            # divide n by two (interger division)
            n = n // 2
        elif n == 1:
            # if n is 1 return 1
            return 1
        else:
            # n = (3 * n) + 1
            n = 3 * n + 1
    return 0


print("f(-1)",f(-1)) # output: -1
print("f(0)",f(0)) # output: 0
print("f(1)",f(1)) # output: 1
print("f(2)",f(2)) # output: 1
print("f(10)",f(10)) # output: 1
print("f(100)",f(100)) # output: 1