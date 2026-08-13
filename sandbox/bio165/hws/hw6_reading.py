import sys

"""
* #1 Print out metadata and variant lines

For this question, and many in the future, you will be reading a VCF file. 
VCF (Variant Call Format), files were developed to store genomic mutations for one or more individuals.

VCF files have three types of lines, and they are always in this order: 

1. First are meta-data lines that always start with one or more “#” signs. 
These lines contain information about how the data were obtained, analyzed, and cleaned, 
and a description of how the variant lines are formatted. 

2. The header line always starts with “#C” or “#c” and is the very last of the lines that start with “#”. 
The header line shows what is in each column of the variant lines. 

3. Lastly, all the variant lines. Variant lines never start with “#”. Variant lines are tab delimited, 
meaning there is a \t character between each column.

Once you get to the first variant line, all subsequent lines are variant lines. 
Although variant lines can vary, they commonly have the following columns in the following order:

Column 1: Chromosome Number
Column 2: Chromosome Position
Column 3: SNP ID (This will usually be some ID number, or a “.” indicating the ID is unknown.)
Column 4: Reference, or wildtype, allele (This is the nucleotide most people have at this position on this chromosome.)
Column 5: Alternate, or variant, allele (This is the nucleotide one or more samples in this file have at this position on this chromosome.)
Column 6: Variant quality (This is a number that reflects the probability that the called variant is correct and not a false positive.)
Column 7: Filter column, which includes information about whether or not a variant passed quality controls (PASS means it passed, anything else means it didn’t.)
Column 8+: All subsequent columns are variable.

Remember that header lines start with “#”.

For this exercice, print all of the meta-data lines, the header line, 
and all the variant lines that have the word “PASS” in the 7th column. 
You are only looking for “PASS” in the 7th column for variant lines and will keep all meta-data lines and the header line, 
regardless of their content. Pass may show up in other columns, but when in the 7th column it will appear alone and in all caps. 
Do not use regular expressions to do this. Remember, these files are tab delimited ("backslash t"). 
Note: When you test your program, there will be a lot of lines printed to the screen. 
You must ensure that only one end of line character is printed after each line 
(you can remove end of line characters with .strip() or .rstrip()).
"""

vcf_file = sys.argv[1]

with open(vcf_file, "r") as infile:
    for line in infile:
        line = line.strip()
        if line.startswith("#"):
            print(line)
        else:
            columns = line.split("\t")
            if len(columns) > 6 and columns[6] == "PASS":
                print(line)
