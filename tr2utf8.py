from os import listdir, path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="File to convert")
parser.add_argument("-d", "--directory", help="Directory containing the files to convert")
args = parser.parse_args()

tr_utf8_matching = {
    "Ð":"Ğ",
    "ð":"ğ",
    "ý":"ı",
    "Ý":"I",
    "þ":"ş",
    "Þ":"Ş",
    "I":"İ"
}
def convert_file(input_path):
    output_path = input_path.replace(".srt", ".tr.srt")

    with open(input_path, "r", encoding=None) as input_file:
        content = input_file.read()

    for char_tr, char_utf8 in tr_utf8_matching.items():
        content = content.replace(char_tr, char_utf8)

    with open(output_path, 'w', encoding="utf-8") as output_file:
        output_file.write(content)

if not args.directory is None:
    for f in listdir(args.directory):
        convert_file(path.join(args.directory, f))

if not args.file is None:
    convert_file(args.file)