
def mystery(n):
    if n <= 0:
        return 0
    else:
        return mystery(n//2) + 1

print(mystery(20)) 
# output is 5 because 
# the function calls itself
# 5 times
# 0 + 1 + 1 + 1 + 1 + 1 = 5
