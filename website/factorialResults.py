from pyDOE import *
import csv
import numpy as np
import re

csv_filename = 'RealTalkSessions.csv'
data = []

with open(csv_filename, 'rU') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        data.append(row)

    levels = [2,2,2,5,5,2,12,2,2,2,7];
    fact = fullfact([2,2,2,5,5,2,12,2,2,2,7])
    data

    print fact
    dataConverted = np.array(data).astype(np.int)

    n = len(levels)  # number of factors
    print n
    nb_lines = np.prod(levels)  # number of trial conditions
    print nb_lines
    H = np.zeros((nb_lines, n))


    level_repeat = 1
    range_repeat = np.prod(levels)
    for i in range(n):
        range_repeat /= levels[i]
        lvl = []
        for j in range(levels[i]):
            lvl += [j]*level_repeat
        rng = lvl*range_repeat
        level_repeat *= levels[i]
        H[:, i] = rng

    print H
            #print H
