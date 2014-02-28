# *-* coding: utf-8 *-*
# Question 2. Triangular Numbers

# Рассмотрим следующий ряд: 1, 3, 6, 10, 15, 21, ...
# Он вычисляет следующим образом:
# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15


# Реализуйте процедуру triangular, которая принимает на вход натуральное число n,
# возвращает n-ный член вышерассмотренного ряда

def triangular(n):
	k = 0
	r = 0
	while k!=n:
		r = r + k +1
		k = k +1
	return r



print triangular(1)
#>>>1

print triangular(3)
#>>> 6

print triangular(10)
#>>> 55
