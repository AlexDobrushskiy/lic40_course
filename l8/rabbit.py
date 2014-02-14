def prirost(x):
	if x<=0:
		return None
	if x<3:
		return 1
	if x<=6:
		return prirost(x-1)+prirost(x-2)
	return prirost(x-1)+prirost(x-2)-prirost(x-6)
for i in range(1,21):
	print prirost(i)