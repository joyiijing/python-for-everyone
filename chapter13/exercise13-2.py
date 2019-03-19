import urllib.request,urllib.parse,urllib.error
import json

url = input('enter url:')
data = urllib.request.urlopen(url).read()

sum = 0
info = json.loads(data)
comments = info['comments']
for item in comments:
    num = item['count']
    sum = sum + int(num)
print(sum)
