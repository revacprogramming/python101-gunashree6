#networking 
#problem 3


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl



ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("ENTER URL: ")
count=int(input("ENTER COUNT: "))
poz=int(input("ENTER POSITION: "))


html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

for a in range(count):
    print("Retrieving:",tags[poz-1].get('href', None))
    url = tags[poz-1].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')