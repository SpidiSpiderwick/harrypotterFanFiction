import os
import base64
import re
import sys

import requests
import json
import csv
import ntpath
import pathlib

from requests_ip_rotator import ApiGateway


def simplify(string):
    return re.sub(r" +", " ", re.sub(r"[^a-zA-Z0-9\-äöüß]", " ", string)).strip().lower()


if __name__ == '__main__':

    gateway = ApiGateway("https://api.imgur.com")
    gateway.start()

    session = requests.Session()
    session.mount("https://api.imgur.com", gateway)

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

            r = session.request("POST", upload_url, headers=headers, json=upload_data)
            if r.status_code == 429 or r.status_code == 417:
                with open(json_path, "w+") as jf:
                    json.dump(links, jf)
                sys.exit(r.status_code)
            links.append(r.json()["data"]["link"])

    sugg_path = r'C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\REVhpsentences.txt.suggestions'

    with open(sugg_path, "r", encoding="utf-8") as sugg_file:
        suggestions = json.load(sugg_file)

    gtrans_path = r'C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\gtranslated.txt'

    with open(gtrans_path, "r", encoding="utf-8") as gtrans_file:
        gtrans = [simplify(line) for line in gtrans_file]

    dtrans_path = r'C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\deeptranslated-utf8.txt'

    with open(dtrans_path, "r", encoding="utf-8") as dtrans_file:
        dtrans = [simplify(line) for line in dtrans_file]

    links_csv = r'C:\Users\asib1\Documents\Asib\repos\harrypotterFanFiction\texttoimage\links.csv'

    with open(links_csv, "w+", newline="", encoding="utf-8") as f:
        spamwriter = csv.writer(f, delimiter=",", quotechar='"')
        spamwriter.writerow(["num", "image_url", "suggestions", "gtrans", "dtrans"])
        spamwriter.writerows([(num, link, suggestions[num], gtrans[num], dtrans[num]) for num, link in enumerate(links)])
