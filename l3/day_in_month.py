days_in_month = [31, 28, 31 ,30 ,31, 30, 31, 31, 30, 31, 30, 31]

def days(month):
	
	return  days_in_month[month-1]
 

print days(4)
