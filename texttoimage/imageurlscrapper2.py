import os
import base64
import re
import sys

import requests
import json
import csv
import pathlib
import ntpath

from requests_ip_rotator import ApiGateway


if __name__ == '__main__':

    gateway = ApiGateway("https://api.imgur.com")
    gateway.start()

    session = requests.Session()
    session.mount("https://api.imgur.com", gateway)

    json_path = r"C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\translationlinks.json"
    with open(json_path, "r") as jf:
        linkss = json.load(jf)
    upload_url = "https://api.imgur.com/3/upload"
    id2 = "3074cf589419a0f"
    id1 = "770af0b3627556b"
    headers = {'Authorization': f'Client-ID {id2}'}
    chapter = r'C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\translations'

    files = [os.path.abspath(os.path.join(chapter, p)) for p in os.listdir(chapter)]
    files.sort()
    iterator = iter(files)

    for first_index in range(0, len(files), 3):
        if first_index / 3 < len(linkss):
            continue

        first = files[first_index]
        second = files[first_index + 1]
        third = files[first_index + 2]

        num = ntpath.basename(first)[0:3]

        triple = []

        for file_path in (first, second, third):
            with open(file_path, "rb") as img_file:
                img_b64_str = base64.b64encode(img_file.read()).decode("ascii")
                print(img_b64_str)
            upload_data = {
                "image": img_b64_str,
                "type": "base64",
                "title": ntpath.basename(file_path),
                "name": ntpath.basename(file_path)
            }
            r = session.request("POST", upload_url, headers=headers, json=upload_data)
            if r.status_code == 429 or r.status_code == 417:
                with open(json_path, "w+") as jf:
                    json.dump(linkss, jf)
                sys.exit(r.status_code)
            triple.append(r.json()["data"]["link"])

        linkss[int(num)] = triple

    sugg_path = r'C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\REVhpsentences.txt.suggestions'

    with open(sugg_path, "r", encoding="utf-8") as sugg_file:
        suggestions = json.load(sugg_file)

    task2csv = r'C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\task2.csv'

    with open(task2csv, "w+", newline="", encoding="utf-8") as f:
        spamwriter = csv.writer(f, delimiter=",", quotechar='"')
        spamwriter.writerow(["num", "image_url1", "image_url2", "image_url3", "suggestions"])
        spamwriter.writerows([(num, links[0], links[1], links[2], suggestions[num]) for num, links in linkss.items()])
