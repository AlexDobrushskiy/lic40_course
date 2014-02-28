# *-* coding: utf-8 *-*
# Question 1: Pick One

# Реализуйте процедуру pick_one, которая принимает 3 входящих параметра:
# Boolean (логический тип, True/False) и два двугих значения. Если первый параметр
# =True, то нужно вернуть второй параметр, иначе - третий

# For example, pick_one(True, 37, 'hello') should return 37, and
# pick_one(False, 37, 'hello') should return 'hello'.

def pick_one(a,b,c):
	if a == "True":
		return b
	else:
		return c

print pick_one(True, 37, 'hello')
#>>> 37

print pick_one(False, 37, 'hello')
#>>> hello

print pick_one(True, 'red pill', 'blue pill')
#>>> red pill

print pick_one(False, 'sunny', 'rainy')
#>>> rainy