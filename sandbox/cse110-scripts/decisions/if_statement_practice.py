#comparing numbers
first_int = int(input("What is the first integer? "))
second_int = int(input("What is the second integer? "))

print()
if first_int > second_int:
    print("The first number is greater than second number ")
else:
    print("The first number is not greater than the second number ")

if first_int == second_int:
    print("The numbers are equal ")
else: 
    print("The numbers are not equal")

if second_int > first_int:
    print("The second number is greater than the first number")
else: 
    print("The second number is not greater than the first number")

#comparing strings
print()
fav_animal = input("What is your favorite animal? ")

if fav_animal.lower() == "orca" or "Orca" or "ORCA":
    print("My favorite animal is orca too! ")
else:
    print("That is not my favorite animal, but still cool tho! ")
print()