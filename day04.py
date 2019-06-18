import urllib.request
import urllib.parse
define self
def data():
    print()
data = bytes(urllib.parse.urlencode({'pw':'123','un':'456'}),encoding='utf8')
url = 'http://httpbin.org/post'
response = type(urllib.request.urlopen(url,data=data))
result = self(response.read().decode('utf8'))
print(result)