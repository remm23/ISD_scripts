#Task 10
#find the errors

# construct the if, elif, else control structure using the flow chart

magnitude = float(input("Enter magnitude: "))

if magnitude > 8.0:
    print("Most structures fall")
elif magnitude > 7.0:
    print("Many buildings desroyed")
elif magnitude > 6.0:
    print("Many buildings considerably damaged, some collapse")
elif magnitude > 4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No distruction of buildings")