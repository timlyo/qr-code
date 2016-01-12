code = "3bb80,fbeabe,8b1aa2,8a80a2,8af6a2,fb32be,2aa80,1ff79ff,7101e7,dc99e1,496164,185a8f6,1281abe,8d355d,836114,e5cc6a,92600b,1fe1aeb,2caa6,fa0cef,8be801,8b3894,8ba05a,fadc0e,20c76"

for thing in code.split(","):
	print(format(int(thing, 16), "025b").replace("1", "  ").replace("0", u"\u2588" * 2))
