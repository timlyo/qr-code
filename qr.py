code = "ffbffff,80aee03,bebaafb,a286a8b,a26028b,a27da8b,be8cafb,806aa03,ff9e7ff,9c0079f,b6e6787,9218593,e12a3db,c9c6afb,a30d577,a098453,b9331ab,a45802f,ff46baf,8072a9b,be433bf,a2ba007,a28e253,a2a816b,be7703b,80431db,ffbffff,ffbffff"

for thing in code.split(","):
	print(format(int(thing, 16) + 262144, "028b").replace("1", "  ").replace("0", u"\u2588" * 2))
