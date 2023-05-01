# import urllib.request as ur
#
# #вбудовані модулі для роботи в internet
# url = 'http://google.com'
# conn =ur.urlopen(url) #обробка запиту
# data = conn.read()
# print(conn.status)
# print(conn.getheader('Content-Type'))
# for key,value in conn.getheaders():
#     print(key, value)
#
# # print(data)

import requests
url="http://google.com"
r=requests.get(url)
print(r.status_code)
# print(r.headers)
print(r.encoding)
print(r.text)


