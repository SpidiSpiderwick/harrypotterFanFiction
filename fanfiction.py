import argparse

from textblob import TextBlob


def writeSentences(chapter, outpath):
    sentences = getSentences(chapter)
    with open(outpath, 'w') as outfile:
        for sentence in sentences:
            outfile.write(str(sentence+'\n'))


def getSentences(chapter):
    return TextBlob(readTxt(chapter)).sentences


def getWordlist(text):
    blob = TextBlob(text)
    words = blob.words
    for sentence in blob.sentences:
        print(sentence.sentiment)
    print(len(words.sentiment))
    print(len(list(dict.fromkeys(blob.words))))


def readTxt(path):
    with open(path, 'r') as file:
        return file.read()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A tool to extract sentences from a textfile."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        help="Path to the input chapter in plain text.",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Path to the where the output shall be saved.",
        default="out.txt",
        required=False,
    )

    args = parser.parse_args()

    writeSentences(args.input, args.output)
