# DNA identifier

This is a Python project that I wrote during CS50's Introduction to Computer Science course. Writing it gave so much joy that I decided to save it here.

## Background

DNA is really just a sequence of molecules called nucleotides, arranged into a particular shape (a double helix). Every human cell has billions of nucleotides arranged in sequence. Each nucleotide of DNA contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Some portions of this sequence (i.e., genome) are the same, or at least very similar, across almost all humans, but other portions of the sequence have a higher genetic diversity and thus vary more across the population.

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs). An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals.

## How to run it?

This program identifies to whom a sequence of DNA belongs. It requires 2 additional command line arguments to run:

```bash
$ python dna.py databases/large.csv sequences/5.txt
```

As its first command-line argument the name of a CSV file containing the STR counts for a list of individuals and should require as its second command-line argument the name of a text file containing the DNA sequence to identify.

## Required modules

You need only 2 modules for this program to work:
csv to work with .csv files and sys to read args from the cmd.

```python
import csv
import sys
from csv import DictReader
```

## How it works

The program is executed with the correct number of command-line arguments.

It then opens the CSV file (database with names and DNA sequences, STRs) and read its contents into memory.

Then it opens .txt DNA sequence (just a long string of text like "SGATTSGGATTAA...") and reads it into memory.

For each of the STRs (from the first line of the CSV file), the program computes the longest run of consecutive repeats of the STR in the DNA sequence to identify.

If the STR counts match exactly with any of the individuals in the CSV file, the program should print out the name of the matching individual.

## STR Databases and DNA sequences

.csv databases and .txt sequences can be found at /databases and /sequences folders. Those files were copied from Edx CS50 online course, but final code is my own.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
