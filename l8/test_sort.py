a=["a","d","c","b"]
b={"a":3,"b":2,"c":5,"d":2}

def f(x):
	return -b[x]

a.sort(key= f)
print a