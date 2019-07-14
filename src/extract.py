import pandas as pd
import csv
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

    roll_list = ['START']


    for line in test:
        for item in line:
            if item[:4] == roll_list[-1]:
                continue
            else:
                roll_list.append(item[:4])

    return roll_list

rolls = roll_curator()


def cr_extractor(lst):
    """[summary]
    
    Arguments:
        lst {list} -- [description]
    """

    roll_str = ','.join(lst)

    camregex = re.compile(r'[a-z]\d\d\d', re.IGNORECASE)
    mo = camregex.findall(roll_str)
    mo.sort()

    f = open("rolls.text", "w")

    f.write("Camera Rolls: \n")
    for roll in mo:
        f.write(roll + "\n")
    f.close()

cr_extractor(rolls)

def sr_curator():

    col_5 = pd.read_csv(csv_path, usecols=[5])
    col_5_lst = col_5.values.tolist()

    path_lst = []
    for line in col_5_lst:
        for item in line:
            path_lst.append(item)
    
    smregex = re.compile(r'sound_masters', re.IGNORECASE)
    rcounter = 0
    sm_arry = []
    for row in path_lst:
        if smregex.search(row):
            sm_arry.append(rcounter)
        rcounter += 1
    

    i = 0
    sr_rolls = []
    while i < len(sm_arry):
        sr_rolls.append(path_lst[sm_arry[i]][-3:])
        i += 1

    f = open('rolls.text', 'a+')
    f.write('\nSound Rolls: \n')
    for roll in sr_rolls:
        f.write(roll + '\n')
    f.close()


sr_curator()