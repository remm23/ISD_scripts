def count_spaces(userInput):
    spaces = 0
    # loop through the users string
    for char in userInput:
        # if character is a space
        if char == " ":
            # increase spaces by 1
            spaces += 1
    return spaces

def main():
    user = input("Enter some text> ")
    # pass the string as an argument to count spaces
    print(count_spaces(user))

main()