#!/usr/bin/env python3

"""
pietje doet dit
"""

__author__ = "Eric Hoekstra & Tim Swarts"
__version__ = "1.0"

class parse_bed:
    """
    huts
    """
    def __init__(self):
        """

        """
        self.bed_dict = {}
        self.test_dict = {1: [(270, 274)], 2: [(275, 277)], 3: [(278,281)]}
        self.chrom = {1: [], 2: [], 3: []}

    def parse_beds(self):
        """

        :return:
        """
        bed_file = open('cardiopanel.bed')

        for line in bed_file:
            # Strip the line and split on the tabs
            entry = line.strip('\n').split('\t')
            try:
                # Adding everything to the dictionary
                self.bed_dict[entry[0]] = []
                self.bed_dict[int(entry[0])].append((int(entry[1]), int(entry[2]), entry[3]))
            except ValueError:
                # It will give a value error for the X chromosome because it's not an integer
                self.bed_dict[entry[0]].append((int(entry[1]), int(entry[2]), entry[3]))

        print(self.bed_dict)

    def pileup(self):
        """

        :return:
        """

        for line in self.bed_dict:
            print(self.bed_dict[line])

        pileup_file = open('small.pileup.txt')
        print("This may take a while with very large files... :)")

        for line in pileup_file:
            position = int(line.split()[1])
            chromosome = int(line.split()[0])
            for entry in self.bed_dict:
                try:
                    start = self.bed_dict[entry][1][0]
                    end = self.bed_dict[entry][1][1]
                    if int(position) >= start and int(position) <= end:
                        print(self.chrom[chromosome].append(line[3]))
                except:
                    break


        #print(self.chrom)







iets = parse_bed()
iets.parse_beds()
iets.pileup()
iets.remove_empty_keys()