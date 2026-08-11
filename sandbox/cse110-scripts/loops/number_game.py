#number game!
print()
number = int(input("Please type in a positive number: "))
print()

while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type in a positive number: "))

print()
if number >= 0:
    print("The number is: " + str(number))
