# Problem 5: Working with Files

'''
Tutorial: 

f = open('input.txt', 'r') # r = read mode, w = write mode, a = append mode

for line in f:
  print line

f = open('output.txt', 'w')
f.write('Any data you want to write into file')

inscription = ['Rosalind Elsie Franklin ', 1920, 1958]
s = str(inscription)
f.write(s)

for i in inscription:
  f.write(str(i) + '\n')
'''

# Program: 

# 1. Read all lines into a list at once
f = open("rosalind_ini5.txt", "r").readlines()

# 2. Slice: Start at index 1, go to end, step by 2
# This gives us [Line 2, Line 4, Line 6...]
target_lines = f[1::2]

# 3. Print them
for line in target_lines:
  print(line.strip())

