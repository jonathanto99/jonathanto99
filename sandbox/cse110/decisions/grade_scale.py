grade = float(input("What is you grade percentage? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

fancy = ""

if grade >= 97:
    fancy = "+"
elif letter == "F":
    fancy = ""
elif grade % 10 >= 7:
    fancy = "+"
elif grade % 10 <= 3:
    fancy ="-"
else:
    grade = ""

print()

if grade < 80 and grade >= 77:
    print(f"{letter}{fancy}")
    print("You'll shoot your eye out!")
elif grade >= 70:
    print(f"{letter}{fancy}")
    print("This class can't hurt you anymore.")
elif grade >=0:
    print(f"{letter}{fancy}") 
    print("Buck up mister. You'll get it next time")
else:
    print("DISHONOR! DISHONOR ON YOU! DISHONOR ON YOUR RICE!")

print()