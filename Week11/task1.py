class Person():
    def __init__(self,firstName):
        # firstName is assigned to the instance variable
        self._name = firstName

# the instance variable is given the value of "Harry" when created
harry = Person("Harry")

print(harry._name)