code = "2fa80,1f080be,1123aa2,11083a2,11343a2,1f17cbe,14a80,3fb8cff,c7155,274badd,17cf554,3747b6e,1dec108,1dec108,1647a55,1504104,1043e0e,19e7a0b,3f908e7,176a8,1f308e6,1117809,1118320,1107372,1f13a06,7380"

for thing in code.split(","):
	print(format(int(thing, 16) + 262144, "026b").replace("1", "  ").replace("0", u"\u2588" * 2))
