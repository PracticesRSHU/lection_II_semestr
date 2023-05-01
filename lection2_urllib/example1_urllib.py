"""
Скористаємося модулем urllib стандартної бібліотеки Python,
щоб отримати певну інформацію із сайту, тобто за вказаним URL 
повернемо код веб-сторінки в Інтернеті у вигляді HTML
"""

import urllib.request as ur #вбудовані модулі для роботи в internet
url = 'http://google.com'
conn =ur.urlopen(url) #обробка запиту
data = conn.read()
print(conn.status)
print(conn.getheader('Content-Type'))
print(data)

for key, value in conn.getheaders():
    print(key, value)
