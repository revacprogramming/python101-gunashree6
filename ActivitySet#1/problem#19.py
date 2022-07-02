#networking
#problem 2

import urllib
from urllib.request import urlopen
import re
count = 0
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_1548032.html"

html = urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup("span")

for tag in tags:
	
	stringnumber = tag.contents
	number= int(stringnumber[0-1])
	count = count+ number
print(count)