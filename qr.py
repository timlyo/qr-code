code = "7154,3bc572,246066,23dce6,3c16f2,dd4,7e0613,ba1dd,255ba2,7b840,40c3e3,27f898,71ebd6,37e1de,555a59,3bf97,7e0b06,8f0,3c6804,23c04f,2455c6,3c21cb,0"

for x in code.split(","):
	print(format(int(x, 16) + 83820, "023b").replace("1", "  ").replace("0", u"\u2588" * 2))
