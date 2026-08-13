import sys

"""
# *Find A Gene in a VCF File

Write a program that takes three parameters from the command line: 
the first is an input vcf file, the second is a new vcf file you will create, and the third is a gene name. 
Print all the header lines from the first file to the second, and print all variant lines that have the gene name 
in them from the first file to the new vcf file (case insensitive). 
Although the search must be case insensitive, you must print all lines to the new file in the same case as they appear 
in the input vcf file. Please, note that you will be looking for the gene name in then 8th column of the VCF file, 
more specifically, this is called the "INFO" column. This column has specific formatting requirements, 
part of which is a requirement to include certain definitions in the header section of the VCF file 
(the section where all the lines start with a "#" character). For the the sake of this task, 
you need not concern yourself with whether or not this was correctly done in the header section. 
However, you do need to know that you can't simply do "if gene_name in line" and expect to get the correct answer.

Please note the following about the INFO column: It is a semi-colon separated list. 
Each element in the list (delineated by semi-colons) matches the format TAG=VALUE, 
where TAG is some key word and VALUE could be a comma-separated list of elements. 
TAG and VALUE may not contain semi-colons, naturally. Each element in this list (delineated by commas) may be anything, 
so long as it does not contain a comma or a semi-colon. Obviously, no tabs (\t) may occur in the INFO column, 
or any other column in the file, as that would, by definition, make it more than a single column.

You will be looking for the gene name in the INFO column. 
You will need to identify whether the gene name is a case-insensitive match to an entire element of the VALUE associated 
with the TAG "GI". The GI TAG's VALUE is a comma-separated list. 
So consider, the following example INFO columns where the gene name is "xyz":

These should be included:

GI=xyz
AB=cde;GI=xyz
GI=xyz;AB=cde
AB=cde;GI=xyz;FG=hijk
AB=cde;GI=xyz,uvw
GI=xyz,uvw;AB=cde
AB=cde;GI=xyz,uvw;FG=hijk
AB=cde;GI=uvw,xyz
GI=uvw,xyz;AB=cde
AB=cde;GI=uvw,xyz;FG=hijk
AB=cde;GI=rst,xyz,uvw
GI=rst,xyz,uvw;AB=cde
AB=cde;GI=rst,xyz,uvw;FG=hijk

These should not be included:

GI=xyzyx
AB=cde;GI=xyzyx
GI=xyzyx;AB=cde
AB=cde;GI=xyzyx;FG=hijk
AB=cde;GI=xyzyx,uvw
GI=xyzyx,uvw;AB=cde
AB=cde;GI=xyzyx,uvw;FG=hijk
AB=cde;GI=uvw,xyzyx
GI=uvw,xyzyx;AB=cde
AB=cde;GI=uvw,xyzyx;FG=hijk
AB=cde;GI=rst,xyzyx,uvw
GI=rst,xyzyx,uvw;AB=cde
AB=cde;GI=rst,xyzyx,uvw;FG=hijk

Also, remember that the presence of the gene name in other columns does not mean the line should be included - 
only if it occurs in the INFO column.
"""

input_file = sys.argv[1]
output_file = sys.argv[2]
gene_name = sys.argv[3]

def geneChecker(input_file, output_file, gene_name):
    with open(input_file, "r") as inf, open(output_file, "a") as outf:
        for line in inf:
            field = line.strip().split("\t")
            if field[0].startswith("#"):
                outf.write(line)
            else:
                chrom, pos, id_, ref, alt, qual, filter_, info, *rest = line.strip().split("\t")
                column_info = info.split(";")
                gene_list = []
                for tag in column_info:
                    if tag.startswith("GI="):
                        gi_value = tag.removeprefix("GI=")
                        gene_list = gi_value.split(",")
                if gene_name.lower() in [g.lower() for g in gene_list]:
                    outf.write(line)

geneChecker(input_file, output_file, gene_name)
                
"""
# *Sum Numbers From the User
In a previous question, we wrote a program that requested zero or more numbers from the user, 
summed them using a function, and then printed the sum. This assignment will do something similar, 
but will require additional effort to handle the system arguments. You will still sum each of the arguments, 
but this time not all of the arguments will be simple numbers.

Remember that all system arguments are strings. Some of the provided arguments, may be multiple numbers, 
separated by spaces. In these cases, you must first multiply the numbers together and then add them to the sum 
with the rest of the numbers. Consider the following examples:

Example 1: 1 2 3 4 5 should be 1+2+3+4+5=15
Example 2: 1 2 "3 4" 5 should be 1+2+(3*4)+5=20
Example 3: "1 2" "3 4" 5 6 should be (1*2)+(3*4)+5+6=25
Example 4: "1 2 3 4" 5 6 should be (1*2*3*4)+5+6=35
Example 5: "1 23 4" 5 6 7 should be (1*23*4)+5+6+7=110
Example 6: "1 2 3" "4 5 6" should be (1*2*3)+(4*5*6)=126

If no numbers are provided, the sum should be zero. We assume you'll print a newline character 
(usually done automatically by the print function) after the result.
"""

rand_nums = sys.argv[1:]

def calculator(rand_nums):
    num_sum = 0
    for num in rand_nums:
        num_product = 1
        if " " not in num:
            num_sum += int(num)
        else:
            for n in num.split(" "):
                num_product *= int(n)
            num_sum += num_product
    return num_sum

print(calculator(rand_nums))
