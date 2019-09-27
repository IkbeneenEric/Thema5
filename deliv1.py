#!/usr/bin/env python3

"""
BFV2 Theme 05 - Genomics - Sequencing Project

Simple template for parsing BED data.

Deliverable 1
-------------
Make changes to the 'parse_bed_data' function, following the instructions
preceded with double '##' symbols.

    usage:
        python3 deliverable1.py
"""

# METADATA VARIABLES
__author__ = "Marcel Kempenaar"
__status__ = "Template"
__version__ = "2018.d1.v1"

# IMPORT
import sys

# FUNCTIONS
def parse_bed_data(bed_data):
    """ Function that parses BED data and stores its contents
        in a dictionary
    """
    ## Create empty dictionary to hold the data
    bed_dict = {}

    ## Iterate over all lines in the 'bed_data' list and fill the
    ## `bed_dict` dictionary with the `chromosome` as key. The other fields
    ## are added as a tuple using the correct types.
    ## Check the `expected_bed_dict` output example in the `main` function below.

    bed_dict = {}

    for line in bed_data:
        line = line.split('\t')
        key = line[0]
        if not key in bed_dict:
            bed_dict[key] = [(int(line[1]), int(line[2]), line[3])]
        else:
            bed_dict[key].append((int(line[1]), int(line[2]), line[3]))

    ## Return the bed_dict one all lines are done
    return bed_dict

######
# Do not change anything below this line
######

# MAIN
def main(args):
    """ Main function that tests for correct parsing of BED data """
    ### INPUT ###
    bed_data = [
        "1	237729847	237730095	RYR2",
        "1	237732425	237732639	RYR2",
        "1	237753073	237753321	RYR2",
        "18	28651551	28651827	DSC2",
        "18	28654629	28654893	DSC2",
        "18	28659793	28659975	DSC2",
        "X	153648351	153648623	TAZ",
        "X	153648977	153649094	TAZ",
        "X	153649222	153649363	TAZ"
    ]

    ### OUTPUT ###
    expected_bed_dict = {
        '1':  [(237729847, 237730095, 'RYR2'),
               (237732425, 237732639, 'RYR2'),
               (237753073, 237753321, 'RYR2')],
        '18': [(28651551, 28651827, 'DSC2'),
               (28654629, 28654893, 'DSC2'),
               (28659793, 28659975, 'DSC2')],
        'X':  [(153648351, 153648623, 'TAZ'),
               (153648977, 153649094, 'TAZ'),
               (153649222, 153649363, 'TAZ')]}

    # Call the parse-function
    bed_dict = parse_bed_data(bed_data)
    _assert_output_vs_expected(bed_dict, expected_bed_dict)

def _assert_output_vs_expected(output, expected):
    """ Compares given output with expected output.
    Do not modify. """
    import unittest
    if isinstance(output, dict):
        testcase = unittest.TestCase('__init__')
        try:
            testcase.assertDictEqual(expected, output,
                                     msg="\n\nUnfortunately, the output is *not* correct..")
        except AssertionError as error:
            print(error)
            return 0
        print("\nWell done! Output is correct!")
        return 1
    print("\n\nUnfortunately, the output is *not* a dictionary!")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))