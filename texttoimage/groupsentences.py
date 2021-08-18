import csv
import glob, os
from collections import Counter

numbers = []
usefulldata = []
myjson = {}
for filename in glob.glob('D:\Projects\harrypotterFanFiction\mTurkAbgeben\*.csv'):
   with open(os.path.join(os.getcwd(), filename), 'r', encoding='utf-8') as f:
      reader = csv.DictReader(f)
      for row in reader:
         numbers.append(row["Input.num"])
         usefulldata.append({"Input.num":row["Input.num"], "Translation": row.get("Answer.translation", None)})

cnt = Counter(numbers)
selection = [k for k, v in cnt.items() if v > 2]
finalselect = [k for k in usefulldata if k.get("Input.num") in selection]
sortedfinalselect = sorted(finalselect, key=lambda k: k['Input.num'])

keys = sortedfinalselect[0].keys()

with open('manytranslations.csv', 'w', newline='')  as output_file:
   dict_writer = csv.DictWriter(output_file, keys)
   dict_writer.writeheader()
   dict_writer.writerows(sortedfinalselect)