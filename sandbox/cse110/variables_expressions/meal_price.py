import math

print()
meal_price_child = float(input("What is the price of a child's meal? "))
meal_price_adult = float(input("What is the price of an adult's meal? "))
children_count = int(input("How many children are there? "))
adults_count = int(input("How many adults are there? "))
salestax_rate = float(input("What is the rate of salestax? "))

print()
subtotal = meal_price_child * children_count + meal_price_adult * adults_count
salestax = subtotal * salestax_rate / 100
tips_amount = subtotal * 0.15
grand_total = float(subtotal) + float(salestax) + float(tips_amount)

print()
print(f"Subtotal: ${str(subtotal)}")
print(f"salestax: ${str(salestax)}")
print(f"Tips: ${str(tips_amount)}")
print(f"Total: ${str(grand_total)}")

print()
payment_amount = float(input("What is the payment amount? "))
change = float(payment_amount - grand_total)
print(f"Change: ${round(change,2)}")
print()