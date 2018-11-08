# explaining array methods
a = [66.25,333,333,1,1234.5]
print("original list:",a)

a.insert(2,-1)
print("insert -1 at index 2:",a)

a.append(333)
print("Appending an element to the end:",a)

# returns the first instance of the argument
print("Findind an index: ",a.index(333))

a.remove(333)
print("Removing a element", a)

a.reverse()
print("Reversing a list:", a)

a.sort()
print("Sort the list from smallest to largest:",a)