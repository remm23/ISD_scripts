# A program that keeps track of items for a shopping list

shopping_list = []
print("Welcome to your shopping list")
print("Press return without any input to quit")
dont_quit = True
while(dont_quit):
    user_input = input("Enter an item> ")
    # check the length of the user input
    if len(user_input) == 0:
        # if input string is 0
        # leave the loop and print the list
        dont_quit = False
    else:
        # add user input to the end of the string
        shopping_list.append(user_input)

print(shopping_list)

# Output
# Welcome to your shopping list
# Press return without any input to quit
# Enter an item> Apples 
# Enter an item> Bananas
# Enter an item> Pears
# Enter an item> 
# ['Apples', 'Bananas', 'Pears']
