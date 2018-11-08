# Task 11
# A program that asks the user for the correct password

password = "changeme"
attempts = 0
while True:
    user_input = input("Enter the password: ")
    # if the user enters the correct password
    if user_input == password:
        print("Accepted. you have access after %d attempts" % attempts)
        # break out of the loop
        break
    attempts += 1
    if attempts >= 5:
        print("Access denied")
        input("Please press enter to exit and contact security ti reset your password")
        break

