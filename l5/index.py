#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Our index has the following structure:
#[ [kw1, [url1, url2, url2]], [kw2, [url21, url22, ..]] ]
from requests import get

def get_page(page):
	return get(page).text

index = []
def add_to_index(index, word, url):
	for i in index:
		if word == i[0]:
			if url not in i[1]:
				i[1].append(url)
			return
	index.append([word,[url]])

add_to_index(index,'random','http:/vk.com')
add_to_index(index,'login','http:/vk.com')
add_to_index(index,'password','http:/vk.com')
add_to_index(index,'login','http:/store.steampowered.com')


def index_lookup(index, keyword):
	for i in index:
		if keyword==i[0]:
			return i[1]
	return []




print index_lookup(index, 'login')	
# >> http:/vk.com

def add_page_to_index(index, url, page_text):
	words = page_text.split ()
	for i in words:
		add_to_index(index,i,url)


wiki_url = 'http://en.wikipedia.org'

add_page_to_index(index, wiki_url, get_page(wiki_url))
print index