import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('enter url:')
data = urllib.request.urlopen(url).read()

sum = 0
tree = ET.fromstring(data)
list = tree.findall('comments/comment')
print('comment count:',len(list))
for item in list:
    numstr = item.find('count').text
    sum = sum + int(numstr)
print(sum)
