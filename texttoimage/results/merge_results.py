import csv
import json


def add_flag(row):
    row["flag"] = "x"
    return row


if __name__ == '__main__':

    all_results = []

    final_path = "final_translations_two.csv"

    deepl_p = r"C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\deeptranslated-utf8.txt"

    with open(deepl_p, "r", encoding="utf-8") as dl:
        deepl = [row.strip() for row in dl]

    m1_p = "manytranslationsOnly1.csv"

    our_results_p = "once_translations.json"

    readparams = {"encoding": "utf-8", "newline": ""}
    Input_num = "Input.num"
    Translation = "Translation"
    fieldnames = [Input_num, Translation]

    with open(m1_p, "r", **readparams) as m1:
        m1_reader = csv.DictReader(m1, fieldnames=fieldnames)
        m1_headers = next(m1_reader)
        all_results.extend([row for row in m1_reader])

    with open(our_results_p, "r", encoding="utf-8") as our_results:
        all_results.extend([{Input_num: int(num), Translation: translation} for (num, translation) in json.load(our_results).items()])

    with open("zero.json", "r", encoding="utf-8") as zero, open("one.json", "r", encoding="utf-8") as one:
        all_results.extend([{Input_num: num, Translation: deepl[int(num)]} for num in json.load(zero)])
        all_results.extend([{Input_num: num, Translation: deepl[int(num)]} for num in json.load(one)])


#
    # with open(m2_p, "r", **readparams) as m2:
    #     m2_reader = csv.DictReader(m2, fieldnames=fieldnames)
    #     m2_headers = next(m2_reader)
    #     all_results.extend([row for row in m2_reader])

    all_results.sort(key=lambda row: int(row[Input_num]))

    with open(final_path, "w+", encoding="utf-8", newline="") as final:
        final_writer = csv.DictWriter(final, fieldnames=fieldnames)
        final_writer.writeheader()
        final_writer.writerows(all_results)
