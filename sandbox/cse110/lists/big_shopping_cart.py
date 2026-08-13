import math

items = []
prices = []
grocery_item = ""
action_taken = ""

print()
print("Welcome to the Shopping Cart Program! ")
print("Type in '5' to quit adding to your grocery list! ")

while action_taken != "5":
    if action_taken == "1":
        grocery_item = input("What item would you like to add? ")
        price_charged = float(input("How much would the item be? "))
        print(f"'{grocery_item} ${price_charged:.2f}' has been added to the cart. ")
        items.append(grocery_item)
        prices.append(price_charged)

    elif action_taken == "2":
        print(f"The contents of the shopping cart are: ")
        for count, value in enumerate(zip(items, prices),1):
            print(f"{count}, ${value}")

    elif action_taken == "3":
        item_removed = int(input("Which item would you like to remove? ")) -1
        print(f"Item removed: {items[item_removed]} ${prices[item_removed]}")
        items.pop(item_removed)
        prices.pop(item_removed)

    elif action_taken == "4":
        total = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    else:
        print("That wasn't one of the actions available, please try again. ")

    print()
    action_taken = input("Please select one of the following: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit shopping \nPlease enter an action: ")

if grocery_item or action_taken == "5":
    print()
    print("Thank you for shopping with us. Goodbye.")
else:
    print("That wasn't one of the actions available, please try again. ")
