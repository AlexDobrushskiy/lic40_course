# *-* coding: utf-8 *-*
# Question 3: Remove Tags

# При индексации веб-страниц мы бы хотели не включать HTML-теги в индекс.
# (такие как <body>, <head>, <table>, <a href="...">, и так далее).

# Напишите процедуру remove_tags, которая принимает на вход строку, и возвращает
# список слов из этой строки, не изменяя их порядок, но исключая HTML-теги.
# Предполагам, что слова могут быть разделены пробелами или HTML-тегами.
# Тегом считается строка между символов < и >. Также предполагаем, что строка не содержит 
# незакрывающихся тегов (< без >)


def remove_tags(s):
	result = ""
	teg_end = 0
	while True:
		teg_start = s.find ("<",teg_end)
		if teg_start == -1:
			result += " " + s[teg_end+1:]
			break
		result += " " + s[teg_end+1:teg_start]
		teg_end = s.find (">",teg_start)
	return result.split()





print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []
