import sys

# * Read Files Problem 1:
# Write a program that accepts one parameter from the command line, the path to a file. 
# Your program should count the number of characters, including end-of-line characters, 
# number of characters excluding end-of-line characters, and lines in the file and print the numbers to the screen. 

file_name = sys.argv[1]
char_num_total = 0
char_num_strip = 0
line_num = 0

with open(file_name, "r") as inFile:
    for line in inFile:
        line_num += 1
        char_num_total += len(line)
        char_num_strip += len(line.rstrip())

print(f"Total characters: {char_num_total}")
print(f"Total characters minus end-of-line characters: {char_num_strip}")
print(f"Total lines: {line_num}")

# * Read Files Problem 2:
# Your program will be provided the name of a file to read on the command line. 
# Write a program that opens the file, sums all the numbers in the file, and prints the sum to the screen. 

read_file = sys.argv[1]
num_sum = 0

with open(read_file, "r") as file:
    for line in file:
        num_sum += int(line)
print(num_sum)
