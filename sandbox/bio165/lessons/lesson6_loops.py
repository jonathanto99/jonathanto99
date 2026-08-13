import sys

# * For Loop Problem 1:
# Write a program that accepts one DNA sequence from the command line and prints the sequence, 
# one character at a time, to the screen. You should use a for loop for this question. 

sequence = sys.argv[1]

for nuc in sequence:
    print(nuc)

# * For Loop Problem 2:
# Write a program that accepts an unknown number of numbers from the command line. 
# Create a list with the square of each number and print the list to the screen. You may only use a for loop.

unknown_num = sys.argv[1:]

square_num = []
for num in unknown_num:
    num_new = int(num) ** 2
    square_num.append(num_new)
print(square_num)

# * For Loop Problem 3:
# Write a program that accepts one non-negative number from the command line,
# determines whether or not the number is prime, and tells the user if the number is prime. You may only use a for loop.

rand_num = int(sys.argv[1])

if rand_num < 1:
    print(f"{rand_num} is not a prime number.")
else:
    is_prime = True
    for divisor in range(2, rand_num):
        if rand_num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{rand_num} is a prime number.")
    else:
        print(f"{rand_num} is not a prime number.")

# * While Loop Problem 1:  
# Write a program that accepts one DNA sequence from the command line and prints the sequence,  
# one character at a time, to the screen. You may only use a while loop. 

dna_sequence = sys.argv[1]

index = 0
while index < len(dna_sequence):
    print(dna_sequence[index])
    index += 1

# * While Loop Problem 2:
# Write a program that accepts an unknown number of numbers from the command line. 
# Create a list with the square of each number and print the list to the screen. You may only use a while loop. 

num_list = sys.argv[1:]

position = 0
num_square = []
while position < len(num_list):
    num = int(num_list[position]) ** 2
    num_square.append(num)
    position += 1
    
print(num_square)

# * While Loop Problem 3:
# Write a program that accepts one non-negative number from the command line, 
# determines whether or not the number is prime, and tells the user if the number is prime. You may only use a while loop. 

num = int(sys.argv[1])

if num < 2:
    print(f"{num} is not a prime number.") # ? But why? 2 is indeed a prime number. 
else:
    is_prime = True
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
