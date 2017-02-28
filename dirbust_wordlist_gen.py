#!/usr/bin/env python
import collections
from collections import OrderedDict
import os
# The purpose of this script is to merge all the dirbus wordlists into a single master wordlist, so that they can be run as a single input file.

folders = ["/usr/share/dirb/wordlists", "/usr/share/dirb/wordlists/vulns"]
filepath1 = "dirbust_wl.txt"
allwords = []


for folder in folders:
    for filename in os.listdir(folder):
        #print folder
        #print filename
        if os.path.isfile(folder + "/" + filename):
            with open(folder + "/" + filename) as infile:
                for line in infile:
                    allwords.append(line)

with open(filepath1, 'w') as outfile:
    for item in allwords:
        outfile.write("%s" % item)
    outfile.close()
