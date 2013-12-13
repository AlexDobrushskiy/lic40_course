def union(a, b):
	result = []
	for i in a+b:
		if i in result:
			pass
		else:
			result.append(i)
	
	return result

a = [1,2,3]
b = [2,4,6]	

print union(a,b)
# >> [1,2,3,4,6]
print b
# >> [2,4,6]