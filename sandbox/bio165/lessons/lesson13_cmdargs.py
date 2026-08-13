import sys

"""
# * Arguments Practice Problem 1
Write a program that accepts an unknown number of files from the command line, followed by a numerical ID. 
Each file will contain multiple lines of tab delimited data, with the numerical ID of the sample always being in the 
first column. You should create a new file called output.txt that contains all the information for the specified ID 
(one piece of information per line). For example, if there are three lines for the specified ID in the first file, 
each of those lines would be printed to output.txt, and if there were two more lines for the specified ID in the second file, 
those would be printed to output.txt after the existing lines, and so on. 
You may assume there will be at least one file on the command line. 
However, the specified ID may not appear in all (or any) of the files so it's possible output.txt is empty. 
"""

sample_id = sys.argv[1]
input_files = sys.argv[2:]

def writeFile(input_files, sample_id):
    with open("output.txt", "w") as outf:
        for filename in input_files:
            with open(filename, "r") as inf:
                for raw in inf:
                    line = raw.strip().split("\t")
                    if line[0] == sample_id:
                        outf.write(raw)

writeFile(input_files, sample_id)

"""
# * Arguments Practice Problem 2
Write a program that either adds an unspecified number of numbers together as floats, 
or concatenates an unspecified number of entries from the command line together as strings.
1. The user should specify whether to treat items on the command line as floats (-f) or as strings (-s).
2. The first item must be -f or -s, and there must be at least two other items after the option.
3. If the command line is malformed, print an error message and quit, otherwise perform the specified action.
4. Write three functions, one that adds the items from the command line when they are floats, 
one that concatenates them when they are strings, and one that does the command line error checking. For example:

python3 studentcode.py -f 1 1 3.2 output: 5.2

python3 studentcode.py -s 1 1 3.2 output: 113.2

python3 studentcode.py 1 1 3.2 -s output: ERROR

python3 studentcode.py -f 1 output: ERROR
"""

arg = sys.argv[1]
items = sys.argv[2:]

def errorChecker(arg, items):
    good_args = ["-f", "-s"]
    if arg not in good_args or len(items) < 2:
        errorChecker is True
        return "ERROR"


def floatAdder(arg, items):
    if arg == "-f":
        float_items = sum(float(i) for i in items)
        return float_items


def stringConcater(arg, items):
    if arg == "-s":
        string_items = [str(i) for i in items]
        return "".join(string_items)

error = errorChecker(arg, items)
if error:
    print(error)
elif arg == "-f":
    result = floatAdder(arg, items)
    print(result)
elif arg == "-s":
    result = stringConcater(arg, items)
    print(result)
