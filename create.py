# Runs all the things

from qr_to_numbers import *

import pprint

printer = pprint.PrettyPrinter()

result = convert("qr.png")


def create_code():
	code = result[0]
	info = result[1]
	printer.pprint(info)

	# remove first 4 numbers for questions
	answers = code[:4]

	# section hidden behind url
	url = ",".join(code[4:]).encode("utf-8")

	print("Answers ", answers)
	print("URL {}".format(url))
	print("URL length:", len(url))
	template = open("code_template.py").read()

	# code_string = "\"{}\"".format(",".join(code))
	code_string = "\"" + "{}," * len(answers) + "{}\""
	print(code_string)

	with open("qr.py", "w") as file:
		file.write(template.format(code=code_string, min=info["min"], width=int(info["Width"])))


def create_document():
	template = open("doc_template.md").read()
	code = open("qr.py").read()

	url = "http://pastebin.com/raw/zG5VxmaF"

	text = template.format(code=code)

	with open("doc.md", "w") as file:
		file.write(text)


if __name__ == "__main__":
	create_code()
	create_document()
