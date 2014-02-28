# *-* coding: utf-8 *-*
# Question 4: Date Converter

# Реализуйте процедуру date_converter, которая принимает 2 параметра. Первый - 
# словарь (dictionary), второй - строка. Строка представляет собой валидную дату в формате
# Месяц/день/год. Процедура должна вернуть дату в формате <день> <название месяца>  <год>.
# Например, если в качестве словаря выбран english:

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# тогда  "5/11/2012" должно быть сконвертировано в  "11 May 2012". 
# ..а если в качестве словаря выбран Шведский

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

# тогда "5/11/2012" должно быть сконвертировано "11 maj 2012".

# Hint: int('12') конвертирует строку '12' в целое (integer) 12.

def date_converter(p,date):
	result = ""
	first_sym = date.find('/')
	second_sym = date.find('/',first_sym+1)
	result = date[:first_sym] + ' ' + p[int(date[first_sym+1:second_sym])] + ' ' + date[second_sym+1:]
	return result

print date_converter(english, '5/11/2012')
#>>> 11 May 2012

print date_converter(english, '5/11/12')
#>>> 11 May 12

print date_converter(swedish, '5/11/2012')
#>>> 11 maj 2012

print date_converter(swedish, '12/5/1791')
#>>> 5 december 1791
