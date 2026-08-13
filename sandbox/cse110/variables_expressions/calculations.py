print()
user_age = int(input("What is your age? "))
new_age = user_age + 1
print("On your next birthday, you will be " + str(new_age))

print()
cartons_count = int(input("How many egg cartons do you have? "))
eggs_count = cartons_count * 12
print("You have " + str(eggs_count) + " eggs")

print()
cookies_count = float(input("How many cookies did you make? "))
ppl_count = float(input("How many people are there? "))
cookies_per_person = cookies_count/ppl_count
print("Each person may have " + str(cookies_per_person) + " cookies")
print()