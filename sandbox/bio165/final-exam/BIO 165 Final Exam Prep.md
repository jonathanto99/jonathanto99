---
tags:
  - education
  - byu
  - bio-165
  - bioinformatics
  - assignment
---
# BIO 165 — Python & Bioinformatics Practice Final Exam

**Format:** 2 main problems + 1 extra credit \| Administered in CodeBuddy

**Note:** All Python standard library built-ins and string methods are permitted freely.

------------------------------------------------------------------------

## Problem 1: FASTA Sequence Analyzer *(60 Pts)*

Write a program called `fasta_analyzer.py` that accepts the following command-line arguments:

```         
python fasta_analyzer.py -i <input.fasta> -o <output.tsv> -m <mode>
```

Where `-m` accepts one of two modes: `gc` or `composition`.

------------------------------------------------------------------------

### Argument Parsing

Use `argparse` to handle all three flags. If any required argument is missing, or if `-m` is not `gc` or `composition`, print this **exact** error message and exit immediately:

```         
Error: USAGE: python fasta_analyzer.py -i input.fasta -o output.tsv -m <gc|composition>
```

------------------------------------------------------------------------

### Function Requirements

**`parse_fasta(filepath)`** Opens the FASTA file and returns a dictionary mapping each header (without `>`) to its full sequence string. Sequences may span multiple lines.

**`calc_gc(header, sequence)`** Returns a tab-separated string in the format below. GC percent should be **unrounded**. If the sequence contains non-ATGC characters (case-insensitive), return `<header>\tERROR` for that record.

```         
<header>\t<GC_percent>%
```

**`count_composition(header, sequence)`** Returns a tab-separated string in the format below. If the sequence is invalid, return `<header>\tERROR`.

```         
<header>\t<length>\tA(<A%>%)\tT(<T%>%)\tG(<G%>%)\tC(<C%>%)
```

------------------------------------------------------------------------

### Output File Format

**`gc` mode** — output file begins with header line `ID\tGC%`

**`composition` mode** — output file begins with header line `ID\tLength\tA(%A)\tT(%T)\tG(%G)\tC(%C)`

Your main logic must be guarded with `if __name__ == "__main__":`.

------------------------------------------------------------------------

### Sample Input — `input.fasta`

```         
>Seq1_BRCA1
ATGCGCTTAA
>Seq2_TP53
AAATTTGGGCCC
>Seq3_invalid
ATGCNNATG
```

### Expected Output — `gc` Mode

```         
ID  GC%
Seq1_BRCA1  40.0%
Seq2_TP53   50.0%
Seq3_invalid    ERROR
```

### Expected Output — `composition` Mode

```         
ID  Length  A(%A)   T(%T)   G(%G)   C(%C)
Seq1_BRCA1  10  3(30.0%)    3(30.0%)    2(20.0%)    2(20.0%)
Seq2_TP53   12  3(25.0%)    3(25.0%)    3(25.0%)    3(25.0%)
Seq3_invalid    ERROR
```

------------------------------------------------------------------------

## Problem 2: Mutation Comparison Tool *(40 Pts)*

Write a program called `mutation_compare.py` that compares a **reference** FASTA file and a **sample** FASTA file, then reports per-sequence differences.

```         
python mutation_compare.py -i1 <reference.fasta> -i2 <sample.fasta> -o <output.tsv>
```

------------------------------------------------------------------------

### Argument Parsing

Use `argparse` to handle all three flags. If any required argument is missing, print this **exact** error message and exit immediately:

```         
Error: USAGE: python mutation_compare.py -i1 reference.fasta -i2 sample.fasta -o output.tsv
```

------------------------------------------------------------------------

### Function Requirements

**`parse_fasta(filepath)`** Same as Problem 1 — returns a `{header: sequence}` dictionary.

**`count_mutations(seq1, seq2)`** Compares two sequences position-by-position and returns the integer count of positions that differ. If the sequences differ in length, compare only up to the length of the shorter sequence.

**`get_mutation_positions(seq1, seq2)`** Returns a list of **1-based** positions where the two sequences differ. For example, if index `2` differs, report position `3`.

------------------------------------------------------------------------

### Output File Format

For each header present in **both** files, write one tab-separated line. Headers present in only one file should be silently skipped. Use a dictionary called `mutation_report` to store results before writing.

Output file must begin with:

```         
ID    Reference    Sample    Mutations    Positions
```

Each subsequent line:

```         
<header>\t<ref_seq>\t<sample_seq>\t<num_mutations>\t<positions>
```

Where `<positions>` is a comma-separated list of 1-based positions (e.g., `3,7,12`), or `none` if there are zero mutations.

Your main logic must be guarded with `if __name__ == "__main__":`.

------------------------------------------------------------------------

### Sample Input

**`reference.fasta`**

```         
>Gene_A
ATGCTTGCA
>Gene_B
GGATCCAAG
```

**`sample.fasta`**

```         
>Gene_A
ATGCTAGCA
>Gene_B
GGATCCAAG
```

### Expected Output — `output.tsv`

```         
ID  Reference   Sample  Mutations   Positions
Gene_A  ATGCTTGCA   ATGCTAGCA   2   6,7
Gene_B  GGATCCAAG   GGATCCAAG   0   none
```

------------------------------------------------------------------------

## Extra Credit: FASTA Translator *(5 Pts)*

Write a program called `fasta_translator.py` that translates DNA sequences from a FASTA file into protein sequences using a codon table file.

```         
python fasta_translator.py -i <input.fasta> -o <output.fasta> -c <codons.tsv>
```

------------------------------------------------------------------------

### Argument Parsing

All three flags are required. If any are missing, print an appropriate error message and exit.

------------------------------------------------------------------------

### Function Requirements

**`load_codons(codon_filepath)`** Reads a tab-delimited file (`codon\tamino_acid`) and returns a dictionary mapping each codon string to its amino acid.

**`translate(header, sequence, codon_dict)`**

- Transcribes DNA -> RNA by replacing `T` with `U` using `re.sub()`
- Reads the RNA in triplets; looks up each codon in `codon_dict`
- Stops translation at the first stop codon (`*`); ignores any trailing incomplete codon
- Returns a FASTA-formatted string: `>{header}\n{protein}\n`
- If the sequence contains non-ATGC characters, returns `>{header}\nERROR\n`

Write all translated records to the output FASTA file. Guard main logic with `if __name__ == "__main__":`.

------------------------------------------------------------------------

### Sample Codon File — `codons.tsv` *(Excerpt)*

```         
AUG M
UUA L
GGA G
UAA *
```

### Sample Input — `input.fasta`

```         
>Protein1
ATGTTAAGG
>Protein2_invalid
ATGNNATG
```

### Expected Output — `output.fasta`

```         
>Protein1
ML
>Protein2_invalid
ERROR
```

------------------------------------------------------------------------

## Concept Coverage Map

| Concept                      | Problem 1 | Problem 2 | Extra Credit |
|:-----------------------------|:---------:|:---------:|:------------:|
| `argparse` + error handling  |    ✅     |    ✅     |      ✅      |
| FASTA parsing + dictionaries |    ✅     |    ✅     |      ✅      |
| Custom functions + `return`  |    ✅     |    ✅     |      ✅      |
| `for`/`while` loops          |    ✅     |    ✅     |      ✅      |
| GC% / nucleotide counting    |    ✅     |           |              |
| File reading + writing       |    ✅     |    ✅     |      ✅      |
| Sequence comparison (SNPs)   |           |    ✅     |              |
| `re.sub()` regex             |           |           |      ✅      |
| Codon translation            |           |           |      ✅      |
| Input validation             |    ✅     |    ✅     |      ✅      |