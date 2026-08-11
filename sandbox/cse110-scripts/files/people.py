import math

youngest_age = 999
youngest_name = ""

#the list of ppl
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

for p in people:
    clean_p = p.strip()
    list_p = clean_p.split()

    name = list_p[0]
    age = int(list_p[1])

    if age < youngest_age:

        youngest_age = age
        youngest_name = name

print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")
