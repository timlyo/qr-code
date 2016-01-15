from PIL import Image

import base64
import math
import re
import pprint


# https://youtu.be/wxsvS_w36Es

def bools_to_int(bools):
	""" Convert a list of booleans to a single integer """
	total = 0
	for index, bool in enumerate(bools[::-1]):
		total += bool * 2 ** index
	return total


def find_factors(integer_list):
	""" Find common factors in integer list
	Worth limiting if it takes too long
	"""
	testing_factors = range(2, max(integer_list)//2)
	found_factors = []
	for factor in testing_factors:
		for integer in integer_list:
			if integer % factor != 0:
				break
		else:  # not valid factor
			found_factors.append(factor)
	return found_factors


def find_repeats(string):
	""" Search encoded string for repetition
	Only useful if repeats are longer than 1 char
	"""
	r = re.compile(r"(.+?)\1+")
	for match in r.finditer(string):
		yield (match.group(1), len(match.group(0)) / len(match.group(1)))


def convert(name):
	# read image
	image = Image.open(name).convert("L").point(lambda x: bool(x))  # greyscale and booleanify
	pixels = image.getdata()

	info = {}

	width = math.sqrt(len(pixels))
	info["Width"] = width

	lines = zip(*[iter(pixels)] * int(width))

	# encode image
	encoded_numbers = []
	integers = []

	for line in lines:
		integer = bools_to_int(line)
		integers.append(integer)

	largest = max(integers)
	smallest = min(integers)
	average = sum(integers) / len(integers)
	factors = find_factors(integers)

	info["min"] = smallest  # maximises the number of near 0 values
	info["max"] = largest
	info["average"] = average
	info["factors"] = factors

	for integer in integers:
		integer_string = str(integer - smallest)
		encoded_numbers.append(integer_string)

	result = ",".join(encoded_numbers)

	try:
		info["Repeats"] = list(find_repeats(result))
	except:
		print("Repeat find failed")
	info["length"] = len(result)

	return result, info

if __name__ == "__main__":
	result = convert("qr.png")

	printer = pprint.PrettyPrinter()

	print(result[0])
	printer.pprint(result[1])

