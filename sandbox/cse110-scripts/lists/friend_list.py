friends_list = []

new_friend = ""

print()
print("!!Type 'end' to end the list!! ")
print()

while new_friend != "end":
    new_friend = input("What is the name of a friend you have? ")
    if new_friend != "end":
        friends_list.append(new_friend)

print()
print("Your friends are: ")
for new_friend in friends_list:
    print(new_friend)
