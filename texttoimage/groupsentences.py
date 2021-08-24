import csv
import glob, os
from collections import Counter
import json

numbers = []
usefulldata = []
myjson = {}
for filename in glob.glob('D:\Projects\harrypotterFanFiction\mTurkAbgeben\*.csv'):
    with open(os.path.join(os.getcwd(), filename), 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            numbers.append(row["Input.num"])
            usefulldata.append({"Input.num": row["Input.num"], "Translation": row.get("Answer.translation", None)})

cnt = Counter(numbers)
selection = [k for k, v in cnt.items() if 1 < v < 3]
finalselect = [k for k in usefulldata if k.get("Input.num") in selection]
sortedfinalselect = sorted(finalselect, key=lambda k: int(k['Input.num']))

with open("medium.txt", 'r', encoding='utf-8') as f:
    mid = json.load(f)

selection = [int(x) for x in selection]
print(x := list(set(mid).intersection(selection)))

with open("deeptranslated-utf8.txt", 'r', encoding='utf-8') as dtranslate:
    translations = dtranslate.readlines()

print(translations := [s.rstrip() for s in translations])
filted_sortedfinalselection = []
for i in x:
    filted_sortedfinalselection = filted_sortedfinalselection + [a for a in sortedfinalselect if
                                                                 i == int(a['Input.num'])]
    filted_sortedfinalselection.append({'Input.num': i, 'Translation': translations[i]})

print(filted_sortedfinalselection)
#keys = filted_sortedfinalselection[0].keys()
keys = sortedfinalselect[0].keys()

with open('manytranslationsOnly2.csv', 'w', newline='', encoding='utf-8')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(sortedfinalselect)

###################################################################################################
#                         Lines that we don't have enough translations already
##################################################################################################
# with open("manytranslations.csv", 'r', encoding='utf-8') as f:
#    reader = csv.DictReader(f)
#    for row in reader:
#       numbers.append(row["Input.num"])
#
# print(newlist := list(dict.fromkeys(numbers)))
#
# with open("long.txt", 'r', encoding='utf-8') as f:
#    long = json.load(f)
#
# with open("medium.txt", 'r', encoding='utf-8') as f:
#    mid = json.load(f)
#
# newlist = [int(x) for x in newlist]
#
# import numpy as np
# main_list_long = np.setdiff1d(long,newlist)
# main_list_mid = np.setdiff1d(mid, newlist)
# print(main_list_long)
# print(main_list_mid)
