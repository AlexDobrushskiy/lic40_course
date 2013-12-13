def find_element(input_list, value):
	a=0
	for i in input_list:
		if i==value:
			return a
		a+=1
	return -1 

def find_element_alter(input_list, value):
	try:
		return input_list.index(value)
	except ValueError:
		return -1
	

print find_element_alter([1,2,3,'asd'], 'asd')
# >> 3
print find_element_alter([1,2,3,'asd'], 44)	
# >> -1


