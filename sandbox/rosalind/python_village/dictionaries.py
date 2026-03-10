# Problem 6: Dictionaries

'''
Tutorial: 

phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
  print (phones['Zoe'])

phones['Zoe'] = '658-99-55'
phones['Bill'] = '342-18-25'
  print (phones)

d = {}
d['key'] = 1
d['Key'] = 2
d['KEY'] = 3
  print (d)

if 'Peter' in phones:
  print("We know Peter's phone")
else:
  print("We don't know Peter's phone")

phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
del phones['Zoe']
  print (phones)

Pseudo code: 

We will build a dictionary from scratch.

1. Split the sentence into a list of words.

2. Loop through every word.

3. If it is a new word, start the count at 1. 

4. If we have seen the word before, add +1 to its count.
'''

# Program: 

raw_text = open("rosalind_ini6.txt", "r").read() # This loads the file's content and makes it readable

words_list = raw_text.split() # This is the string that we need to process into individual words

word_counts = {} # empty dictionary that we can add words to

# Counting processed string as a list and checking if the word is indeed in the list
for word in words_list: 
  # If the word is seen for the first time, set its word count to 1 in the dictionary
  if word not in word_counts: 
    word_counts[word] = 1 
  # Add 1 to the word count in the dictionary if the word is indeed already there
  else:
    word_counts[word] += 1

# For every key and value in the word_counts dictionary, we will print out the key and value
for key, value in word_counts.items():
  print(key, value)
