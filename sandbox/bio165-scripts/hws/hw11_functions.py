import sys

"""
# **Who is your mascot? (inputs: 0, returns: 1, side-effects: 0)**

Write a short program that has no system arguments. It must include a function called `getMascotsName` 
that accepts zero parameters, produces no side-effects, and returns one output of type str. 
The string that is returned must be "Cosmo the Cougar". Your program must print the following to the screen: 
"BYU's Mascot is Cosmo the Cougar\n". For context, please note that several common python functions accept zero parameters, 
produce no side-effects, and return a basic type, e.g., `time()` from the time module and `randint()` from the random module.

We will test your code with the following command:

python studentcode.py

The expected output from these commands is:

BYU's Mascot is Cosmo the Cougar

In this exercise, you will write only the code for your function (including its definition). 
We will embed your function into a program that looks like this:
"""

def getMascotsName():
    mascot = "Cosmo the Cougar"
    return mascot

print("BYU's Mascot is " + getMascotsName())


"""
# **Display an error (inputs: 0, returns: 0, side-effects: 1)**

Write a short program that has no system arguments. 
It must include a function called displayError that accepts zero parameters, produces one side-effect, and returns nothing. 
The side-effect should be an error message displayed to the user (e.g., with the print function). 
The error message must be exactly: "Houston, we have a problem". 
Note that this must be printed to the screen from inside the displayError function, not from your non-function code. 
Generally speaking, side-effects are undesirable in functions; however, they are very useful in certain situations. 
The most notable example is the print function, though generally the print function is passed parameters. 
Without parameters, the print function prints a single character ('\n').

We will test your code with the following command:

python studentcode.py

The expected output from these commands is:

Houston, we have a problem

In this exercise, you will write only the code for your function (including its definition). 
We will embed your function into a program that looks like this:
"""

def displayError():
    print("Houston, we have a problem")

displayError()


"""
# **Extract PASSing variants from a VCF file (inputs: 1, returns: 1, side-effects: 0)**

Write a short program that has two system arguments. The program will read through a VCF file, 
extract header lines and data lines with "PASS" in the seventh column, and write the extracted lines to a new VCF file. 
You have already completed similar tasks with VCF files, so this should be familiar to you. 
This time, you must use a function to determine whether or not a line should be included in the new output file. 
This function must accept one input of type `str`, return one output of type `bool`, and produce no side-effects.

The input string will be a single line read in from the input VCF file. The output boolean will be `True` or `False` 
(obviously, as `True` and `False` are by definition the only two possible options for a boolean). 
Your function should return `True` if the line should be included in the output VCF file and `False` 
if the line should be excluded from the VCF output. Your function must be called `writeToFile`. 
For context, an example of a python function that accepts a single parameter and returns a single output is `len`.

Remember, header lines in a VCF file start with a "#" character. All these lines should be copied to the new output file. 
The data lines, those that don't have a "#" character in the first position, 
should be added to the new output file only if they have "PASS" in the seventh column. 
More specifically, the seventh column must be exactly "PASS". We will test your code with the following command:

python studentcode.py input.vcf output.vcf

In this exercise, you will write **only** the code for your function (including its definition). 
We will embed your function into a program that looks like this:
"""

def writeToFile(line):
    if line.startswith("#"):
        return True
    else:
        line = line.split("\t")
        if line[6] == "PASS":
            return True

# get the filenames from system arguments
input_vcf_filename = sys.argv[1]
output_vcf_filename = sys.argv[2]

# open (and automatically close using 'with') the files
with open(output_vcf_filename, 'w') as output_file:
    with open(input_vcf_filename, 'r') as input_file:
        # loop through each line in the input file
        for line in input_file:
            # check if the line should be written to the output file
            if writeToFile(line):
                # write the line
                output_file.write(line)


"""
# **Display a more informative error (inputs: 1, returns: 0, side-effects: 1)**

This question is intentionally similar to question #2, which was admittedly a silly example. 
In this question, you must extend your work from question #2 to allow for more informative error messages. 
This will require you to write a function that will be much more similar to the `print` function 
than your function from question #2.

Write a short program that has no system arguments. 
It must include a function called `displayInformativeError` that accepts one parameter of type `str`, 
produces one side-effect, and returns nothing. The side-effect should be an error message displayed to the user 
(e.g., with the `print` function). The error message must be exactly: "ERROR: ", 
followed by whatever informative message is provided to the function as a parameter. 
Note that this must be printed to the screen from inside the `displayInformativeError` function, 
not from your non-function code.

We will test your code with the following command:

python studentcode.py

In this exercise, you will write only the code for your function (including its definition). 
We will embed your function into a program that looks like this:
"""

def displayInformativeError(s):
    print(f"ERROR: {s}")


def seqHasNumbers(s):
    for n in s:
        if n.isdigit():
            return True
    return False


def hasNonDNAletters(s):
    dna_letters = "ACGT"
    for n in s:
        if n not in dna_letters:
           return True
    return False


def hasHighGCpercent(s):
   return (float(s.count('C') + s.count('G')) / len(s)) > 0.75


for seq in [ "AATT", "CCGG", "ACGT", "XACGT", "012345" ]:
    if seqHasNumbers(seq):
        displayInformativeError("Sequence \"" + seq + "\" has numbers in it!")
    elif hasNonDNAletters(seq):
        displayInformativeError("We found invalid letters in sequence \"" + seq + "\"!")
    elif hasHighGCpercent(seq):
        displayInformativeError("The following sequence was valid, but has high GC content: " + seq)
    else:
        print(seq)

"""
Accordingly, the output from your program should look like this:

AATT
ERROR: The following sequence was valid, but has high GC content: CCGG
ACGT
ERROR: We found invalid letters in sequence "XACGT"!
ERROR: Sequence "012345" has numbers in it!
"""


"""
# **Add integers in a list (inputs: 1, returns: 1, side-effects: 0)**

This question is intended to demonstrate a function may accept an object as a parameter that is not one of the basic types 
(i.e., `str`, `int`, `float`, or `bool`). This function takes a `list` that may or may not be empty. 
If it is not empty, all elements will be of type `int`.

Write a short program that has zero or more system arguments. 
It must include a function called `add` that accepts one parameter of type `list` (with zero or more elements of type `int`), 
produces no side-effects, and returns an `int`. You are to sum the integers provided and return the sum. 
You may not use the `sum` function. You may not use a variable called `sum`.

We will test your code with the following commands:

python studentcode.py
python studentcode.py 1 2 3 4 5 6 7 8 9
python studentcode.py 0 2 91 2 100

In this exercise, you will write only the code for your function (including its definition). 
We will embed your function into a program that looks like this:
"""
def add(integer):
    total_int = 0
    for number in integer:
        total_int += number
    return total_int

# get the system arguments, convert them to ints, put them in a list
integers = []
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        integers.append(int(sys.argv[i]))

# get the total and display it
print(add(integers))

"""
The expected output from these commands is:

0
45
195
"""


"""
# **Keep only factors of three - new list (inputs: 1, returns: 1, side-effects: 0)**

This and the following question are intended to demonstrate the difference between basic type parameters 
(i.e., `str`, `int`, `float`, or `bool`) and other objects (i.e., `list`, `dict`, etc.). 
In this problem, you will write a function that takes a `list` that may or may not be empty. 
If it is not empty, all elements will be of type `int`. In this question, you will not change the original `list`, 
but instead return a new `list` with certain elements removed (if necessary).

Write a short program that has zero or more system arguments. It must include a function called `copyFactorsOfThree` 
that accepts one parameter of type `list` (with zero or more elements of type `int`), produces no side-effects, 
and returns a `list` (with zero or more elements of type `int`). The new `list` you return must be exactly the same, 
just without any elements that are not factors of three. You may assume all numbers provided will be non-zero, positive integers. 
As a general hint, remember the modulus (%) operator is useful for determining the remainder after integer division.

Outside your function, the output will be formatted as a space-separated series of elements, 
followed by a newline character. We'll output the original `list` and the new `list`.

We will test your code with the following commands:

python studentcode.py 1 2 3 4 5 6 7 8 9
python studentcode.py 1 2 8 91 100
python studentcode.py 3 6 9 12 15
python studentcode.py 3 6 9 3 6 9
python studentcode.py 10 11 12 13 14 15 16 17 18 19

In this exercise, you will write only the code for your function (including its definition). 
We will embed your function into a program that looks like this:
"""

def copyFactorsOfThree(integers):
    result = []
    for i in integers:
        if i % 3 == 0:
            result.append(i)
    return result

# get the system arguments, convert them to ints, put them in a list
integers = []
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        integers.append(int(sys.argv[i]))

# copy the list, keeping only the factors of three into a new list
threes = copyFactorsOfThree(integers)

# display the original and the modified copy
for i in range(len(integers)):
    integers[i] = str(integers[i])
print(' '.join(integers))

for i in range(len(threes)):
    threes[i] = str(threes[i])
print(' '.join(threes))

"""
The expected output from these commands is:

1 2 3 4 5 6 7 8 9
3 6 9
1 2 8 91 100
3 6 9 12 15
3 6 9 12 15
3 6 9 3 6 9
3 6 9 3 6 9
10 11 12 13 14 15 16 17 18 19
12 15 18
"""


"""
# **Keep only factors of three - same list (inputs: 1, returns: 0, side-effects: 1)**

This and the previous question are intended to demonstrate the difference between basic type parameters 
(i.e., str, int, float, or bool) and other objects (i.e., list, dict, etc.). 
In this problem, you will write a function that takes a list that may or may not be empty. 
If it is not empty, all elements will be of type int. In this question, you will change the original list, 
instead of returning a new list with certain elements removed (if necessary).

Write a short program that has zero or more system arguments. 
It must include a function called removeNonFactorsOfThree that accepts one parameter of type list 
(with zero or more elements of type int), produces one side-effect, and returns nothing. 
Previous functions you have written with side-effects printed things to the screen. 
The side-effect in this instance will change the list passed into the function as a parameter. 
Do not write anything out to the screen in your function. The list you modify must be exactly the same, 
just without any elements that are not factors of three. You may assume all numbers provided will be non-zero, positive integers. 
As a general hint, remember the modulus (%) operator is useful for determining the remainder after integer division. 
You may also find it helpful to lookup the list.pop function and/or the del keyword as it applies to a list and its elements; 
however, if you don't want to look them up, this task is still possible - it just requires a little extra cleverness.

Outside your function, the output will be formatted as a space-separated series of elements, followed by a newline character. 
We'll output the original list you have modified with your function.

We will test your code with the following commands:

python studentcode.py 1 2 3 4 5 6 7 8 9         
python studentcode.py 1 2 8 91 100         
python studentcode.py 3 6 9 12 15         
python studentcode.py 3 6 9 3 6 9         
python studentcode.py 10 11 12 13 14 15 16 17 18 19

In this exercise, you will write only the code for your function (including its definition). 
We will embed your function into a program that looks like this:
"""

def removeNonFactorsOfThree(integers):
    integers[:] = [i for i in integers if i % 3 == 0]

# get the system arguments, convert them to ints, put them in a list
integers = []
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        integers.append(int(sys.argv[i]))

# keeping only the factors of three, modify the original list
removeNonFactorsOfThree(integers)

# display the original list that has been modified
for i in range(len(integers)):
    integers[i] = str(integers[i])

if len(integers) == 0:
    print("NONE")
else:
    print(' '.join(integers))

"""
The expected output from these commands is:

3 6 9
NONE
3 6 9 12 15
3 6 9 3 6 9
12 15 18
"""
