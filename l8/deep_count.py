a= [1,2,3]
# len(a)
# a = [ [1,2,3,[1,2,3,3]] ]
# len(a)
#isinstance(object, type_name)

def deep_count(li):
	cnt = 0
	for i in li:
		if isinstance (i,list):
			cnt += deep_count(i)
		else:
			cnt += 1
	return cnt

print deep_count (a)

b = [1,2,3,[1,4,6,[1,3,[]]]]

print deep_count (b)