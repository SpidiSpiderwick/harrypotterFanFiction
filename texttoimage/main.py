#!/usr/bin/python3

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os
import argparse
import sys
import textwrap
from typing import List


def parse_from_file(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [x.strip() for x in f.readlines()]


def generate_images_from_file(
        chapter: str,
        image_out_folder: str,
        text_width: int = 50,
        font_size: int = 11,
        font: str = "./fonts/DejaVuSans.ttf",
        col_bg: str = "#ffffff",
        col_fg: str = "#000000",
        margin: int = 6
):

    os.makedirs(image_out_folder)

    for counter, line in enumerate(parse_from_file(chapter)):
        generate_image_from_text(
            line,
            os.path.join(image_out_folder, f"{chapter}.{counter}.png"),
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
    text_width: int = 50,
    font_size: int = 11,
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

    offset: float = margin / 2
    for line in line_list:
        draw.text((margin / 2, offset), line, font=img_font, fill=col_fg)
        offset += img_font.getsize(line)[1]

    img.save(image_out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "A program to generate an image from a given text. Text can be provided either by a textfile or STDIN."
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
        "-s",
        "--font-size",
        type=int,
        help="Sets the font size to be used to generate the image.",
        default=11,
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
        chapter=args.input_file,
        image_out_folder=args.output,
        text_width=args.width,
        font=args.font_path,
        font_size=args.font_size,
        margin=args.margin,
        col_bg=args.background_color,
        col_fg=args.foreground_color,
    )
