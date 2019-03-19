import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

#url = input('enter url:')
#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html,'html.parser')
times = 7
position = 18

def findUrl(position,url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    return tags[position].get('href',None)

for time in range(times):
    if(time == 0):
        url = input('enter url:')
        url = findUrl(position-1,url)
    else:
        url = findUrl(position-1,url)
print(url)
