a = 0
b = 0
c = 0
d = 0
e = ""

code = {code}.format(a, b, c, d, e)

for x in code.split(","):
	print(format(int(x) + {min}, "0{width}b").replace("1", "  ").replace("0", u"\u2588" * 2))
