import requests
url = 'http://google.com'
r = requests.get(url)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
