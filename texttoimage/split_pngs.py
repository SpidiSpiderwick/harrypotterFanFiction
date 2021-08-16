import json
import os
import csv

if __name__ == '__main__':
    base_folder = r"C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage"

    chapter_p = os.path.join(base_folder, "ch39")

    short_p = os.path.join(base_folder, "short.txt")
    medium_p = os.path.join(base_folder, "medium.txt")
    long_p = os.path.join(base_folder, "long.txt")

    with open(short_p, "r", encoding="utf-8") as short_f:
        short = json.load(short_f)

    with open(medium_p, "r", encoding="utf-8") as medium_f:
        medium = json.load(medium_f)

    with open(long_p, "r", encoding="utf-8") as long_f:
        long = json.load(long_f)

    with open(os.path.join(base_folder, "links.csv"), "r", encoding="utf-8", newline="") as links_csv, \
            open(os.path.join(base_folder, "short.csv"), "w+", encoding="utf-8", newline="") as short_csv_f, \
            open(os.path.join(base_folder, "medium.csv"), "w+", encoding="utf-8", newline="") as medium_csv_f, \
            open(os.path.join(base_folder, "long.csv"), "w+", encoding="utf-8", newline="") as long_csv_f:

        short_csv = csv.DictWriter(short_csv_f, delimiter=",", quotechar='"', fieldnames=["num", "image_url", "suggestions", "gtrans", "dtrans"])
        short_csv.writeheader()
        medium_csv = csv.DictWriter(medium_csv_f, delimiter=",", quotechar='"', fieldnames=["num", "image_url", "suggestions", "gtrans", "dtrans"])
        medium_csv.writeheader()
        long_csv = csv.DictWriter(long_csv_f, delimiter=",", quotechar='"', fieldnames=["num", "image_url", "suggestions", "gtrans", "dtrans"])
        long_csv.writeheader()

        spamreader = csv.DictReader(links_csv, delimiter=",", quotechar='"')
        for row in spamreader:
            if int(row["num"]) in short:
                short_csv.writerow(row)
            if int(row["num"]) in medium:
                medium_csv.writerow(row)
            if int(row["num"]) in long:
                long_csv.writerow(row)
