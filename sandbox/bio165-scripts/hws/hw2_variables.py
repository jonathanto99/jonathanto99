import sys

age = int(sys.argv[1])
current_age = f"You are {age} years old."
age_in_five_years = f"You will be {age + 5} in five years."
age_in_half = f"Half your age is {age / 2}."

print(current_age)
print(age_in_five_years)
print(age_in_half)