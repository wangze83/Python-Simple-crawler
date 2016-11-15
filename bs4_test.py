#coding=utf8
import re
from bs4 import BeautifulSoup
#Met the problem : ImportError: cannot import name BeautifulSoup
#That because you can't call this file bs4.py and from bs4, don't from this file's name


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print 'get all links'
links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()