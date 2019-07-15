import pandas as pd
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(dir_path, 'CSV', 'test.csv')

data = pd.read_csv(csv_path, usecols=[0])
test = data.values.tolist()


def roll_curator():
    """[extracts the rolls from CSV and appends to list]

    Returns:
        [list] -- [contains first four digits of the first column]
    """

    roll_list = ['']

    for line in test:
        for item in line:
            if item[:4] == roll_list[-1]:
                continue
            else:
                roll_list.append(item[:4])

    return roll_list


def cr_extractor(lst):
    """[The roll list gets convertered to a string, and then a regex is used
        to search through the string to find a match object. The results are
        printed to a text file called rolls.text]

    Arguments:
        lst {list} -- [a list containing potential camera rolls]
    """

    roll_str = ','.join(lst)

    camregex = re.compile(r'[a-z]\d\d\d', re.IGNORECASE)
    mo = camregex.findall(roll_str)
    mo.sort()

    f = open(dir_path + "rolls.text", "w")
    f.write("Camera Rolls: \n")
    for roll in mo:
        f.write(roll + "\n")
    f.close()


def sr_curator():
    """[Searches through column five, for the sound_masters path and appends
        the last three digits of the path to rolls.text.]
    """

    col_5 = pd.read_csv(csv_path, usecols=[5])
    col_5_lst = col_5.values.tolist()

    #* Iterates through col_5_lst twice to grab the strings.
    path_lst = []
    for line in col_5_lst:
        for item in line:
            path_lst.append(item)

    #* Iterates through every row till it finds sound_masters
    #* Stores index number in sm_arry for later use
    smregex = re.compile(r'sound_masters', re.IGNORECASE)
    i = 0
    sm_arry = []
    for row in path_lst:
        if smregex.search(row):
            sm_arry.append(i)
        i += 1

    #* Adds the last three chars of every row that was indexed
    #* inside of sm_array. Stores Sound Rolls in sr_rolls[]
    i = 0
    sr_rolls = []
    while i < len(sm_arry):
        sr_rolls.append(path_lst[sm_arry[i]][-3:])
        i += 1

    f = open(dir_path + 'rolls.text', 'a+')
    f.write('\nSound Rolls: \n')
    for roll in sr_rolls:
        f.write(roll + '\n')
    f.close()


rolls = roll_curator()
cr_extractor(rolls)
sr_curator()