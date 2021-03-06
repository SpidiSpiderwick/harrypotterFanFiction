#!/usr/bin/python3
import re

import csv
import json

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os
import argparse
import textwrap
from typing import List

BLUE = "#A6A6FF"


def split_on_dictionary(text, dictionary):
    indices = []
    for (eng, ger, reg_str) in dictionary:
        indices += [match.span() for match in reg_str.finditer(text)]
    indices.sort()

    if indices:
        indice_iter = iter(indices[:])
        current = next(indice_iter)
        nextitem = next(indice_iter, None)

        while nextitem:
            if current[0] <= nextitem[0] < current[1]:
                if current[1] - current[0] < nextitem[1] - nextitem[0]:
                    indices.remove(current)
                else:
                    indices.remove(nextitem)

            current = nextitem
            nextitem = next(indice_iter, None)

    return split_on_indices(text, indices)


def split_on_indices(text, indices_p):

    if not indices_p:
        return [(text, "")]

    indices = indices_p[:]
    if indices[-1][1] != len(text):
        indices.append((len(text), len(text)))

    snippets = []

    last_match_end = 0

    for start, end in indices:
        snippets.append((text[last_match_end:start], text[start:end]))
        last_match_end = end

    return snippets


def parse_from_file(filename: str, di) -> List[str]:
    with open(filename, "r") as f:
        lines = f.readlines()

        translations = [None] * len(lines)

        for i, line in enumerate(lines):
            translations[i] = {eng: ger for (eng, ger, regex) in di if regex.search(line)}

        with open(filename + ".suggestions", "w", encoding="utf-8") as sugg:
            json.dump(translations, sugg)

        # text = f.read()
        # for eng, ger in di:
            # text = re.sub(r"(?<![a-zA-Z0-9])" + re.escape(eng) + r"(?![a-zA-Z0-9])", f"[{eng}][[{ger}]]", text)

        return lines


def read_dictionary(dictionary_path, sep=','):
    with open(dictionary_path, 'r') as f:
        spamreader = csv.reader(f, delimiter=sep, quotechar='"')
        di = dict((row[0], row[1]) for row in spamreader).items()
        return [(eng, ger, re.compile(r"(?<![a-zA-Z0-9])" + re.escape(eng) + r"(?![a-zA-Z0-9])")) for (eng, ger) in di]


def generate_images_from_file(
        chapter_path: str,
        image_out_folder: str,
        dictionary_path: str,
        text_width: int = 50,
        font_size: int = 11,
        font: str = "./fonts/DejaVuSans.ttf",
        col_bg: str = "#ffffff",
        col_fg: str = "#000000",
        margin: int = 6,
):

    if not os.path.exists(image_out_folder):
        os.makedirs(image_out_folder)

    di = read_dictionary(dictionary_path)

    lines = parse_from_file(chapter_path, di)

    digits = len(str(len(lines)))

    for counter, line in enumerate(lines):
        generate_image_from_text(
            line,
            os.path.join(image_out_folder, f"{chapter_path}.{str(counter).zfill(digits)}.png"),
            di,
            text_width,
            font_size,
            font,
            col_bg,
            col_fg,
            margin
        )


def generate_image_from_text(
    text: str,
    image_out_path: str,
    di,
    text_width: int = 50,
    font_size: int = 26,
    font: str = "./fonts/DejaVuSans.ttf",
    col_bg: str = "#ffffff",
    col_fg: str = "#000000",
    margin: int = 6,
):

    img_font = ImageFont.truetype(font, font_size)
    # create test image to get width/ height
    testImg = Image.new("RGB", (1, 1))
    testDraw = ImageDraw.Draw(testImg)

    # get max_height/ weight for the splitted lines
    max_width: int = 0
    max_height: int = 0

    line_list = textwrap.wrap(text, text_width)
    # get example width/ height
    for line in line_list:
        img_width, img_height = testDraw.textsize(line, img_font)
        if img_width > max_width:
            max_width = img_width
        if img_height > max_height:
            max_height = img_height

    img = Image.new(
        "RGB", (max_width + margin, (len(line_list) * max_height) + margin), col_bg
    )
    draw = ImageDraw.Draw(img)

    x_offset: float = margin / 2
    y_offset: float = margin / 2
    for line in line_list:
        for plain, highlighted in split_on_dictionary(line, di):
            draw.text((x_offset, y_offset), plain, font=img_font, fill=col_fg)
            draw.text((x_offset + img_font.getsize(plain)[0], y_offset), highlighted, font=img_font, fill=BLUE)
            x_offset += img_font.getsize(plain + highlighted)[0]
        x_offset = margin / 2
        y_offset += img_font.getsize(line)[1]

    img.save(image_out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "A program to generate an image from a given text."
    )
    parser.add_argument(
        "-i",
        "--input-file",
        type=str,
        help="Filename from which the text shall be read.",
        required=True
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="output folder",
        default="out",
        required=False
    )
    parser.add_argument(
        "-d",
        "--dictionary",
        type=str,
        help="path to dictionary eng->ger",
        default="",
        required=False
    )
    parser.add_argument(
        "-s",
        "--font-size",
        type=int,
        help="Sets the font size to be used to generate the image.",
        default=26,
    )
    parser.add_argument(
        "-m",
        "--margin",
        type=int,
        help="Sets the margin between the image-border and the text.",
        default=6,
    )
    parser.add_argument(
        "-f",
        "--font-path",
        type=str,
        help="Sets the path to the true-type-font (.ttf) that shall be used to generate the image. Default is the provided DejaVuSans.",
        default="./fonts/DejaVuSans.ttf",
    )
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        help="Sets the character width per line. Aka. how many characters shall be displayed for each line.",
        default=50,
    )
    parser.add_argument(
        "-fg",
        "--foreground-color",
        type=str,
        help="Sets the foreground (text) color of the generated image. (Default: black)",
        default="#000000",
    )
    parser.add_argument(
        "-bg",
        "--background-color",
        type=str,
        help="Sets the background color of the generated image. (Default: white)",
        default="#ffffff",
    )
    args = parser.parse_args()

    generate_images_from_file(
        chapter_path=args.input_file,
        image_out_folder=args.output,
        dictionary_path=args.dictionary,
        text_width=args.width,
        font=args.font_path,
        font_size=args.font_size,
        margin=args.margin,
        col_bg=args.background_color,
        col_fg=args.foreground_color,
    )
