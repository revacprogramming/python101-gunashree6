# Using Web Services
# https://www.py4e.com/lessons/servces
import urllib.request
import xml.etree.ElementTree as et
url=input('enter url :')
fh=urllib.request.urlopen(url).read()
tree= et.fromstring(fh)
data=tree.findall('comments/comment')
sum=0
for i in data:
  num=int(i.find('.//count').text)
  sum+=num
print(sum)
