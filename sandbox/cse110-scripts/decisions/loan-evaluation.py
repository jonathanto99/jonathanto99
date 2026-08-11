print()
loan_size = int(input("From 1-10, how big is your loan going to be? "))
credit_history = int(input("From 1-10, how good is your actual credit history? "))
income = int(input("From 1-10, how much do you make in a month? "))
down_payment = int(input("From 1-10, how much are you willing to pay for down payment? "))
print()

if loan_size >= 5 and credit_history >= 7 and income >= 7:
    loan_decision = True
elif loan_size >= 5 and (credit_history >= 7 or income >= 7) and down_payment >= 5: 
    loan_decision = True
elif loan_size < 5 and (income < 7 and down_payment < 4): 
    loan_decision = False
elif loan_size < 5 and (income >= 7 or down_payment >= 4):
    loan_decision = True
elif loan_size < 5 and income >= 7 and down_payment >= 4:
    loan_decision = True
else: 
    loan_decision = False

if loan_decision: 
    print("You are eligible for a loan! ")
else: 
    print("Sorry, you don't qualify for a loan. ")
print()