# Runs all the things

from qr_to_numbers import *

import pprint

printer = pprint.PrettyPrinter()

result = convert("qr.png")
code = result[0]
info = result[1]

printer.pprint(info)

template = 'code = "{code}"\n\nfor x in code.split(","):\n\tprint(format(int(x) + {min}, "0{width}b").replace("1", "  ").replace("0", u"\u2588" * 2))\n'

with open("qr.py", "w") as file:
	file.write(template.format(code=code, min=info["min"], width=int(info["Width"])))