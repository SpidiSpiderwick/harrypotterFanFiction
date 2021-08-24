import csv
import os

from texttoimage.main import generate_image_from_text


if __name__ == "__main__":

    font_size = 26
    margin = 6
    font_path = "./fonts/DejaVuSans.ttf"
    width = 50
    fg = "#000000"
    bg = "#ffffff"

    if not os.path.exists("translations"):
        os.mkdir("translations")

    with open("results/manytranslations.csv", "r", encoding="utf-8") as mt:
        mtreader = csv.DictReader(mt, fieldnames=["Input.num", "Translation"])
        headers = next(mtreader)
        counter = 0
        for row in mtreader:
            counter += 1
            if counter > 3:
                counter = 1
            num = row["Input.num"]
            translation = row["Translation"]

            generate_image_from_text(
                text=translation,
                image_out_path=f"translations/{str(num).zfill(3)}{counter}.png",
                di=[]
            )
