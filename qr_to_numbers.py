from PIL import Image

import math
import zlib, base64


# https://youtu.be/wxsvS_w36Es

def bools_to_int(bools):
	""" Convert a list of booleans to a single integer """
	total = 0
	for index, bool in enumerate(bools[::-1]):
		total += bool * 2 ** index
	return total


def find_simple_factors(integer_list):
	""" Find small common factors in integer list"""
	testing_factors = range(2, 500000)
	found_factors = []
	for factor in testing_factors:
		for integer in integer_list:
			if integer % factor != 0:
				break;
		else:  # not valid factor
			found_factors.append(factor)
	return found_factors


name = "qr.png"
image = Image.open(name).convert("L").point(lambda x: bool(x))
pixels = image.getdata()

width = math.sqrt(len(pixels))

print("Width", width)

lines = zip(*[iter(pixels)] * 23)

encoded_numbers = []
integers = []

for line in lines:
	integer = bools_to_int(line)
	integers.append(integer)

largest = max(integers)
smallest = min(integers)
average = sum(integers) / len(integers)
factors = find_simple_factors(integers)
print("Min:", smallest, "this is the magic number")  # maximises the number of near 0 values
print("Max:", largest)
print("Average", average)
print("Factors", factors)

for integer in integers:
	string = str(hex(integer - smallest)).replace("0x", "")
	encoded_numbers.append(string)

result = ",".join(encoded_numbers)
print("length: ", len(result))
print(result)
