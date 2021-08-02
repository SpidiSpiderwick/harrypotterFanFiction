import os
import base64
import sys

import requests
import json
import csv
import ntpath
import pathlib


if __name__ == '__main__':
    json_path = r"C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\links.json"
    with open(json_path, "r") as jf:
        links = json.load(jf)
    upload_url = "https://api.imgur.com/3/upload"
    id2 = "3074cf589419a0f"
    id1 = "770af0b3627556b"
    headers = {'Authorization': f'Client-ID {id2}'}
    chapter = r'C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\ch39'
    for index, file_path in enumerate(os.listdir(chapter)):
        if index < len(links):
            continue

        file_path = os.path.abspath(os.path.join(chapter, file_path))
        if file_path.endswith(".png"):
            with open(file_path, "rb") as img_file:
                img_b64_str = base64.b64encode(img_file.read()).decode("ascii")
                print(img_b64_str)
            upload_data = {
                "image": img_b64_str,
                "type": "base64",
                "title": ntpath.basename(file_path),
                "name": ntpath.basename(file_path)
            }

            r = requests.request("POST", upload_url, headers=headers, json=upload_data)
            if r.status_code == 429:
                with open(json_path, "w+") as jf:
                    json.dump(links, jf)
                sys.exit(r.status_code)
            links.append(r.json()["data"]["link"])

    sugg_path = r'C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\REVhpsentences.txt.suggestions'

    with open(sugg_path, "r") as sugg_file:
        suggestions = json.load(sugg_file)

    links_csv = r'C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\links.csv'

    with open(links_csv, "w+", newline="") as f:
        spamwriter = csv.writer(f, delimiter=",", quotechar='"')
        spamwriter.writerow(["num", "image_url", "suggestions"])
        spamwriter.writerows([(num, link, suggestions[num]) for num, link in enumerate(links)])
