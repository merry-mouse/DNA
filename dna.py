import csv
import sys
from csv import DictReader

def main():

    # TODO: Check for command-line usage
    n = len(sys.argv)
    if n < 3:
        # error message
        print("Incorrect number of arguments. Example: dna.py databases/large.csv sequences/5.txt")
    else:
        # saving command line arguments (files' names)
        database_file = sys.argv[1]
        sequence_file = sys.argv[2]
        # create a reader object for DNA database csv file
        with open(database_file) as csv_database:
            # pass the file object to dictreader to get the DICT OBJECT
            database_dict_reader = DictReader(csv_database)
            # get a list of dictionaries from the dictreader
            DNA_list = list(database_dict_reader)

        # create reader object to save the first row of csv database
        # we need this for saving sequences separately
        with open(database_file) as first_line_reader:
            # get column names (we need a list of sequences)
            csv_reader = csv.reader(first_line_reader, delimiter=',')
            # loop to iterate through the rows of csv
            for row in csv_reader:
                # storing the row in the vartiable
                list_of_column_names = row
                # break the loop after the first iteration
                break

        # create a reader object for DNA SEQUENCE TXT file
        with open(sequence_file, "r") as sequence_text:
            sequence_string = sequence_text.read()

    # call longest match function, and find number of the longest match for substring
    # that stored in a list_of_column_names (except 0 element "name")
    DNA_STR_counts = {}
    for i in range(1, len(list_of_column_names)):
        # storing the answer of longest_match function in a variable
        value = longest_match(sequence_string, list_of_column_names[i])
        # writing this value in the dict
        DNA_STR_counts[list_of_column_names[i]] = str(value)

    # check both dictionaries for matching parts
    for dictionary in DNA_list:
        if all(item in dictionary.items() for item in DNA_STR_counts.items()):
            print(dictionary["name"])
            quit()
    print("No match")
    # print("DNA list: ", DNA_list)
    # print("DNA STR counts: ", DNA_STR_counts)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

