import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input('enter url:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

sum = 0
tags = soup('span')
for tag in tags:
    sum = sum + int(tag.contents[0])
print(sum)
