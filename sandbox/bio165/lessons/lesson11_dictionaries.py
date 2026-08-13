import sys

'''
# * Dictionary Practice Problem 1
Write a Python program that creates a dictionary of animal names where the keys are the names of the animal, 
and the values are the names used to describe a baby of that animal. 
Your dictionary should include the following key:value pairs: dog/puppy, cat/kitten, horse/foal, and bear/cub. 
Additionally, your program should accept the name of one of the animals from the command line, 
and print the name used for its baby. You may assume the user will enter a valid animal name 
(i.e., the name of the animal is in your dictionary). You may not use a conditional for this problem. 
'''

animal_names = {
    "cat":"kitten", 
    "dog":"puppy", 
    "bear":"cub", 
    "horse":"foal",
    }

animal_names["cat"] = "kitten"
animal_names["dog"] = "puppy"
animal_names["bear"] = "cub"
animal_names["horse"] = "foal"

name = sys.argv[1].lower()
print(animal_names[name])

'''
# * Dictionary Practice Problem 2
Write a program that creates a dictionary that has every number from 1 to 100 as keys and their squares as the values. 
For example, your dictionary should include the following key:value pairs: 1:1, 2:4, 3:9,...,99:9801, 100:10000. 
The user will provide one number on the command line (1-100) and your program should use that number to
retrieve its square from the dictionary. Print the square of the number to the screen. 
Obviously, you don't need the dictionary to do this, but for this question you should use the dictionary
to find the square of the number requested by the user. 
You may assume the user will enter a valid whole number in the range 1-100. 
'''

# Long version
number = int(sys.argv[1])

squares = {}
for num in range(1, 101):
    square = num * num
    squares[num] = square

print(squares[number])

# Short version
num = int(sys.argv[1])

squares = {n: n**2 for n in range(1, 101)}
print(squares[num])

'''
# * Dictionary Practice Problem 3
Write a program that accepts a path to a file from the command line. The file contains text. 
Your program should count how many times each word is used in the file. The counts should be case insensitive 
(e.g., "The" and "the" are the same word), and you should ignore punctuation 
(e.g., "dog.", "dog,", and "Dog" are the same word). You may safely remove any punctuation in the file 
(as you read in each line). The only possible punctuation in the file are periods and commas. 
Use a dictionary to keep track of counts. After counting all the words, print out the words and their counts 
(word, one space, then the count). Print one word and its count per line. 
In this example, the keys of your dictionary should be the words in the file
and the values should be a count of how many times each word appears in your file. 
Remember, you can change the value of an associated key in a dictionary 
(i.e., you can add one to it, or overwrite it completely), but you cannot change a value for a key 
if that key doesn't already exist in your dictionary. 
What error do you get if you attempt to access a key that doesn't exist in a dictionary? 
'''

# Long version
file_path = sys.argv[1]
word_counts = {}

with open(file_path) as inf:
    for line in inf:
        line = line.strip().lower().replace(",", "").replace(".", "")
        words = line.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

for word, count in word_counts.items():
    print(f"{word} {count}")

# Short version
file_path = sys.argv[1]
word_counts = {}

with open(file_path, "r") as inf:
    for line in inf:
        words = line.lower().split()
        for word in words:
            word.replace(".", "").replace(".", "")
            word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print(f"{word} {count}")
