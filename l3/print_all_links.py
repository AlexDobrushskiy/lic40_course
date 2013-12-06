from requests import get

def getpage(page):
	return get(page).text

page = getpage('http://yandex.ru')
# page = 'Not "good" at all'
# <a href="http://yandex.ru">asdhgj</a>

# make a comment - Ctrl + /
def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0

	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote

# url, end = get_next_target(page)
# print url
# page1 = page[end:]
# url, end = get_next_target(page1)
# print url

def print_all_links(page):
	while True: 
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else: 
			break 



print_all_links(page)

