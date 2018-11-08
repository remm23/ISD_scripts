name = input("Enter your name: ")
age = int(input("Enter your age: "))
# age is incremented by 1 before added to the string
print("Hello %s, next year you will be %d years old!" % (name,age+1))

# another way to update and print age
age_next_year = age + 1
print("Hello " + name + ", next year you will be " + str(age_next_year) + " years old!")
