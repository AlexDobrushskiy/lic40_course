# *-* coding: utf-8 *-*
# Question 5: Find and Replace


# В этом задании вам нужно реализовать две процедуры:
# make_converter(match, replacement)
# 	Принимает на вход две строки и и возвращает конвертер (например, список из этих двух 
# 	строк). Или словарь. На самом деле, все, что угодно, что можно применить 
# 	потом в apply_converter.
# apply_converter(converter, string)
# 	Принимает на вход конвертер (то, что вернула make_converter), и строку. Возвращает результат
# 	применения конвертера к входной строке. То есть: заменяет все вхождения совпадения на то, 
# 	чем нужно это совпадение заменить. Процесс продолжается до тех пор, пока ни одного 
# 	вхождения не останется. Можно также посмотреть на тесты внизу:


def make_converter(s1,s2):
	return [s1, s2]

def apply_converter(c,s3):
	while True:
		if c[0] in s3:
			s3 = s3[:s3.find(c[0])] + c[1] + s3[s3.find(c[0])+len(c[0]):] 	
		else:
			break
	return s3


c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
#>>> ab


