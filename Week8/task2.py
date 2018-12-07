def main():
    a = 5
    b = 7
    # main function calls the mystery function
    print(mistery(a,b))

def mistery(x,y):
    z = x + y
    z = z / 2.0
    return z

main()
# output: 6.0