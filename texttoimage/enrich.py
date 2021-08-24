import csv
import sys

if __name__ == '__main__':
    old_csv = "manytranslationsOnly2.csv"
    new_csv = "manytranslationsOnly2_deepl.csv"

    deepl = "deeptranslated-utf8.txt"

    with open(deepl, "r", encoding="utf-8") as d:
        deepl = [line for line in d]

    with open(old_csv, "r", encoding="utf-8") as old, open(new_csv, "w+", encoding="utf-8", newline="") as new:
        Input_num = "Input.num"
        Translation = "Translation"
        spamreader = csv.DictReader(old, fieldnames=[Input_num, Translation])
        headers = next(spamreader)

        spamwriter = csv.DictWriter(new, fieldnames=[Input_num, Translation])
        spamwriter.writeheader()

        while True:
            one = next(spamreader, None)
            two = next(spamreader, None)

            if not one or not two:
                break

            if one[Input_num] != two[Input_num]:
                sys.exit(1)

            spamwriter.writerow(one)
            spamwriter.writerow(two)
            spamwriter.writerow({Input_num: one[Input_num], Translation: deepl[int(one[Input_num])].strip()})
