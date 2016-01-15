# Runs all the things

from qr_to_numbers import *

import pprint
import base64
import zlib

printer = pprint.PrettyPrinter()

result = convert("qr.png")
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
template = open("template.py").read()

# code_string = "\"{}\"".format(",".join(code))
code_string = "\"" + "{},"*len(answers) + "{}\""
print(code_string)

with open("qr.py", "w") as file:
	file.write(template.format(code=code_string, min=info["min"], width=int(info["Width"])))
