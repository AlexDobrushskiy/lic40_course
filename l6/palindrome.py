def is_palindrom(s):
	if len(s) <= 1:
		return True
	if s[0] == s[-1]:
		return is_palindrom (s[1:-1])
	return False


s1 = 'abctcba'
s2 = 'kjhg'
s3 = 'ajha'

l = [s2,s1,s3]
for i in l:
	print is_palindrom (i)