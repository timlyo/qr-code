a = 0
b = 0
c = 0
d = 0
e = ""

code = "{},{},{},{},{}".format(a, b, c, d, e)

for x in code.split(","):
	print(format(int(x) + 83820, "023b").replace("1", "  ").replace("0", u"\u2588" * 2))
