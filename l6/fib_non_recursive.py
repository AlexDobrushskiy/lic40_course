def fib_nr(n):
	if n<=2:
		return 1
	fib1=1
	fib2=1
	result=0	
	for a in range(3,n+1):
		result=fib1+fib2
		fib2=fib1
		fib1=result
	return result
print fib_nr(70000)
