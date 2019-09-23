#!/usr/bin/env python3

"""
BFV2 Theme 05 - Genomics - Sequencing Project

Simple template for parsing and filtering pileup data.
Pileup data falling within the exons in the 'bed_dict' is stored in a
dictionary. This dictionary should contain a coverage number for each
position within the ~50 genes from the cardiopanel (BED file).

Deliverable 2
-------------
Make changes to the 'parse_pileup_data' function, following the instructions
preceded with double '##' symbols.

    usage:
        python3 deliverable2.py
"""

# METADATA VARIABLES
__author__ = "Marcel Kempenaar"
__status__ = "Template"
__version__ = "2018.d2.v1"

# IMPORT
import sys

# FUNCTIONS
def parse_pileup_data(pileup_data, bed_dict):
    """ Function that parses pileup data and collects the per-base coverage
    of all exons contained in the BED data.

    Iterate over all pileup lines and for each line:
        - check if the position falls within an exon (from `bed_dict`)
            - if so; add the coverage to the `coverage_dict` for the correct gene
    """

    ## Create empty dictionary to hold the data
    coverage_dict = {}
    coord_list = []

    for line in pileup_data:
        # Haal chromosoomnummer er uit
        chromosome = line.split("\t")[0][3:5]
        if chromosome in bed_dict:
            # Als het chromosoom in de bed dictionary zit wordt hij er uit gehaald
            coords = bed_dict[chromosome][0:3]
            for x in coords:
                # Check of de coordinaten uit de bed dictionary tussen de coordinaten valt
                if int(line.split("\t")[1]) >= x[0] and int(line.split("\t")[1]) <= x[1]:
                    # Sla naam en coveragenummer op
                    name = x[2]
                    coverage = int(line.split("\t")[3])
                    # Sla ze op in de coverage dictionary
                    if name in coverage_dict:
                        coverage_dict[name].append(coverage)
                    else:
                        coverage_dict[name] = [coverage]

    return coverage_dict

# MAIN
def main(args):
    """ Main function with example input data (pileup and parsed bed)"""

    ### INPUT ###
    # Pileup data with chromosome, position, base, coverage, reads, quality
    pileup_data = [
        'chr1	839427	A	24	,,,,,,,,,,,,,,,,,,,,,,,,	BFGGGGGGGGHHGHH3AFHHIGFG',
        'chr1	237732518	T	24	,,,,,,,,,,,,,,,,,,,,,,,,	>FFFGHHHCDHHHHGF>CHHHHHA',
        'chr1	237732519	T	24	,,,,,,,,,,,,,,,,,,,,,,,,	>FFFGHHHCDHHHHGF>CHHHHHA',
        'chr1	237732520	T	26	,,,,,,,,,,,,,,,,,,,,,,,,,,	>FFFGHHHCDHHHH5GGF>CHHHHHA',
        'chr1	237732521	T	27	,,,,,,,,,,,,,,,,,,,,,,,,,,,	>FFFGHHHCDHHHH6GFGF>CHHHHHA',
        'chr3	1290	T	24	,$,,,,,,,,,,,,,,,,$,,,,,,,	;FFFGGCGGFHHHFHF;FFHHHFD',
        'chr4	123383120	A	22	.....................^].	>HHHHGHHBHHFGGG5GD1ACA',
        'chr12	78383124	G	22	.$....................^].	;HBH1GFAHHHHFGDGGGFFC>',
        'chr12	78383132	C	22	.....................^].	HHHHHBHHGHHHHHGGGGFC1B',
        'chr18	28651722	A	23	......................^].	GHFHHFHGAHHHHHFGGGFFABB',
        'chr18	28659880	C	23	.......................	HHHHHHHHCHH4HHGFGGFF?BA',
        'chr18	28659881	C	23	.......................	HHHHHHHHCHH4HHGFGGFF?BA',
        'chr18	28659882	C	19	...................	HHHHCHH4HHGFGGFF?BA',
        'chr18	28659883	C	19	...................	HHHHCHH4HHGFGGFF?BA',
        'chrX	9402753	A	23	.......................	HHHGGHG/AHHHHHHG4GBBABB'
    ]

    # BED data with chromosome (key), list of tuples with (start, stop and gene name)
    bed_dict = {
        '1':  [(237729847, 237730095, 'RYR2'),
               (237732425, 237732639, 'RYR2'),
               (237753073, 237753321, 'RYR2')],
        '18': [(28651551, 28651827, 'DSC2'),
               (28654629, 28654893, 'DSC2'),
               (28659793, 28659975, 'DSC2')]}

    ### OUTPUT ###
    expected_coverage_dict = {
        "RYR2" : [24, 24, 26, 27],
        "DSC2" : [23, 23, 23, 19, 19]
    }

    # Call the parse-function
    coverage_dict = parse_pileup_data(pileup_data, bed_dict)
    _assert_output_vs_expected(coverage_dict, expected_coverage_dict)

    # FINISH
    return 0

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