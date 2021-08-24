import csv
import json


def add_flag(row):
    row["flag"] = "x"
    return row


if __name__ == '__main__':

    all_results = []

    final_path = "final_translations.csv"
    m1_p = "manytranslations.csv"
    m2_p = "manytranslationsOnly2_deepl.csv"
    our_results_p = "ourtranslationsmedium.json"

    readparams = {"encoding": "utf-8", "newline": ""}
    Input_num = "Input.num"
    Translations = "Translation"
    fieldnames = [Input_num, Translations]

    with open(m1_p, "r", **readparams) as m1:
        m1_reader = csv.DictReader(m1, fieldnames=fieldnames)
        m1_headers = next(m1_reader)
        all_results.extend([row for row in m1_reader])

    with open(m2_p, "r", **readparams) as m2:
        m2_reader = csv.DictReader(m2, fieldnames=fieldnames)
        m2_headers = next(m2_reader)
        all_results.extend([row for row in m2_reader])

    with open(our_results_p, "r", encoding="utf-8") as our_results:
        all_results.extend([add_flag(row) for row in json.load(our_results)])

    all_results.sort(key=lambda row: (int(row[Input_num]), row.get("flag", "")))

    final_fieldnames = [Input_num, "flag", Translations]

    with open(final_path, "w+", encoding="utf-8", newline="") as final:
        final_writer = csv.DictWriter(final, fieldnames=final_fieldnames)
        final_writer.writeheader()
        final_writer.writerows(all_results)
