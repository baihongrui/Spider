import urllib.request
import urllib.parse
def data():
    print()
data = urllib.parse.urlencode({'wd':'q'},encoding='utf8')
print(data)
url = 'http://www.baidu.com/s?'+data
print(url)
response = urllib.request.urlopen(url)
HTHL = response.read().decode('utf8')
print('HTHL')