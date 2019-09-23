#!/usr/bin/env python3

"""
BFV2 Theme 05 - Genomics - Sequencing Project

Template for reading in data and writing output data. Running this script
will print the first three lines of the input BED and pileup files and
write the coverage statistics to the file 'd3_output.csv'.

Note that this template expects the input BED and pileup files to be
present as (see the main() function below):
    ./data/
          |__ example.bed
          |__ example.pileup

Deliverable 3
-------------
Make changes to all the functions below, following the instructions
preceded with double '##' signs.

    usage:
        python3 deliverable3.py
"""

# METADATA VARIABLES
__author__ = "Marcel Kempenaar"
__status__ = "Template"
__version__ = "2018.d3.v1"

# IMPORT
import sys
import csv

# FUNCTIONS
def read_data(filename):
    """ This function reads in data and returns a list containing one
        line per element. """
    ## Open the file given the filename stored in 'filename'
    ## Return a list where each line is a list element

    pileup_file = open(filename)

    line_list = []

    for line in pileup_file:
        line_list.append(line)

    return line_list

def save_coverage_statistics(coverage_file, coverage_statistics):
    """ Writes coverage data to a tabular file using Python's
        csv library: https://docs.python.org/3/library/csv.html#csv.writer
    """

    with open(coverage_file, mode='w', newline="") as csv_file:
        csv_out = csv.writer(csv_file)

        # writing tuples containing information to the csv file
        for x in coverage_statistics:
            csv_out.writerow(x)


def calculate_mapping_coverage(coverage_dict):
    """ Function to calculate all coverage statistics on a per-gene basis
        and store this in a list.
        Note: this function is taken from deliverable 5 and slightly modified
    """

    ## Create an empty list that will hold all data to save
    statistics = []

    # Adding the necessary information to a list in tuples
    for gene in coverage_dict:
        # Amount of low coverage bases
        low_coverage = len([coverage_dict[gene] for i in coverage_dict[gene] if i < 30])
        # Coverage length per gene
        coverage = coverage_dict[gene]
        # Adding the gene name, coverage length, average coverage and amount of low coverage scores
        statistics.append((gene, len(coverage),
                           round(sum(coverage) / len(coverage), 1), low_coverage))

    return statistics

######
# Do not change anything below this line
######

# MAIN
def main(args):
    """ Main function """

    ### INPUT ###
    # Input data files
    bed_file = 'data/example.bed.txt'
    pileup_file = 'data/example.pileup.txt'

    # Input coverage dictionary
    coverage_dict = {
        "SOB2" : [99, 100, 100, 100, 100, 100, 100, 101, 110, 110, 110, 100,
                  99, 98],
        "NEXN" : [256, 266, 233, 255, 345, 355, 344, 222, 399, 200, 199, 263,
                  234, 133, 165, 176],
        "TCAP" : [50, 51, 55, 23, 43, 23, 33, 24, 53, 24, 30, 33, 37, 37],
        "MYPN" : [52, 37, 22, 86, 58, 20, 10, 9, 2, 3, 1, 93, 51, 88, 77, 25,
                  14, 48, 9, 64, 7, 56, 74, 13],
        "MYBPC3" : [67, 93, 56, 59, 24, 11, 2, 72, 6, 32, 32, 40, 70, 80, 37,
                    42, 98, 26, 41, 73],
        "MYH6" : [38, 51, 67, 17, 29, 47, 67, 89, 62, 34, 41, 53, 67, 50, 46,
                  62, 89, 27, 12, 22, 7, 39, 39, 40, 33, 18, 93, 65, 52, 12,
                  17, 14, 90, 79, 37],
        "TXNRD2" : [73, 256, 156, 80, 11, 313, 180, 338, 78, 189, 205, 151,
                    29, 48, 286, 38, 62, 208, 134, 257, 118, 44]
    }

    ### OUTPUT ###
    # Output data files
    csv_file = 'd3_output.csv'

    # Read BED data
    print("Reading BED data from", bed_file)
    bed_data = read_data(bed_file)
    if bed_data is None:
        print("No BED-data read...")
    else:
        print('A total of', len(bed_data), 'lines have been read. The first 3 lines are:\n\t')
        print('\t', '\n\t'.join(bed_data[0:3]), '\n', sep='')

    # Read Pileup data
    print("\nReading pileup data from", pileup_file)
    pileup_data = read_data(pileup_file)
    if pileup_data is None:
        print("No Pileup-data read...")
    else:
        print('A total of', len(pileup_data), 'lines have been read. The first 3 lines are:\n\t')
        print('\t', '\n\t'.join(pileup_data[0:3]), '\n', sep='')

    # Store calculated data
    coverage_statistics = calculate_mapping_coverage(coverage_dict)
    # Write output data
    print('\nWriting data to CSV file...')
    save_coverage_statistics(csv_file, coverage_statistics)
    from pathlib import Path
    csv_file_check = Path(csv_file)
    if csv_file_check.is_file():
        print('\tCSV file created, program finished.')
    else:
        print('\tCSV file', csv_file, 'does not exist!')

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))