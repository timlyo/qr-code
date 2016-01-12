from PIL import Image

import math
import zlib, base64


def bools_to_int(bools):
	total = 0
	for index, bool in enumerate(bools[::-1]):
		total += bool * 2 ** index
	return total


# https://youtu.be/wxsvS_w36Es


name = "qrcode.png"

image = Image.open(name).convert("L").point(lambda x: bool(x))

pixels = image.getdata()

print("Image is", math.sqrt(len(pixels)), "wide")

lines = zip(*[iter(pixels)] * 25)

digits = []

largest_bit = 18

for line in lines:
	integer = bools_to_int(line)  # magic number because none will be higher than it for given qr code, must be readded
	string = str(hex(integer)).replace("0x", "")
	# bytes = string.encode("utf-8")
	digits.append(string)

print(",".join(digits))
