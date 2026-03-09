# Problem 4: Conditions and Loops

'''
Tutorial:

a = 42
if a < 10:
  print ('the number is less than 10')
else:
  print ('the number is greater or equal to 10')

if a + b == 4:
  print('printed when a + b equals four')
print('always printed')

greetings = 1
while greetings <= 3:
  print ('Hello! ' * greetings)
  greetings = greetings + 1

greetings = 1
while greetings <= 3:
  print ('Hello! ' * greetings)
  greetings = greetings + 0 # This will create an infinite loop

names = ['Alice', 'Bob', 'Charlie', 'Diana']
for name in names:
  print("Hello, " + name + "!")

n = 10
for i in range(n):
  print i

print(list(range(5, 12)))
'''

# Program:

# 1. Replace these numbers with the ones from your dataset
a = 4873
b = 9627

# 2. Initialize a variable to keep track of the sum
total_sum = 0

# 3. Loop through the numbers
# We use 'b + 1' because range stops BEFORE the last number.
for i in range(a, b + 1):

  # Check if the number is odd
  # The % operator is "modulo" (it gives the remainder).
  # If a number divided by 2 has a remainder of 1, it is odd.
  if i % 2 == 1:
    total_sum += i

# 4. Print the final result
print(total_sum)
