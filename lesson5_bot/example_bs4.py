# import requests
# from bs4 import BeautifulSoup
# # pip install beautifulsoup4
#
# url = 'https://7days-ua.com/news/sanktsii-ukrainy-proty-medvedchuka-vse-shcho-vidomo-pro-prychyny-i-naslidky-video/'
# response = requests.get(url)
# print(response)
# data = []
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # print(soup.text)
#     ulelement=soup.find("ul",class_="upw-posts hfeed") #{"class":"upw-posts hfeed",}
#     data=ulelement
#     for elem in ulelement.find_all("a"):
#         # print(elem.find("time").get("datetime"))
#         # print(elem.get('href'))
#         #видалити тег <time> з дерева https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/
#         elem.time.decompose()
#         print(elem.text.split("\n")[-1])
#
# # from pprint import pprint
# # pprint(data)

# import requests
# from bs4 import BeautifulSoup
# # pip install beautifulsoup4
#
# url = "http://kreatech.lviv.ua/news/"
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
# #парсим сторінку
# response = requests.get(url,headers=headers)
# # print(response.text)
# data = []
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # print(soup.text)
#     ulelement=soup.find_all("div",class_="product_open") #{"class":"upw-posts hfeed",}
#     print(ulelement)
#     # for elem in ulelement:
#     #     print(elem.find("h2").get_text())
#     data=ulelement
#     for elem in ulelement:
#         # print(elem.find("time").get("datetime"))
#         print(elem.find("a").get('href'))
#         print(elem.find("h2").get_text())
#         # видалити тег <time> з дерева https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/
#         # elem.time.decompose()
#         # print(elem)
#
# # from pprint import pprint
# # pprint(data)


import requests
#в терміналі запускаємо команду pip install requests
from bs4 import BeautifulSoup
#в терміналі запускаємо команду  pip install  BeautifulSoup4
import datetime

#Отримання інформації в м.Рівне про погоду https://ua.sinoptik.ua/
def parsPogoda():
    '''
     <div class="temperature">
      <div class="min">мін. <span>+13°</span></div>
      <div class="max">макс. <span>+18°</span></div>
    </div>
        <p class="today-temp">+15°C</p>
    '''
    url = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%80%D1%96%D0%B2%D0%BD%D0%B5/"
    date_now = datetime.datetime.now()
    # print(date_now.date())
    url_date_now=f'{url}{str(date_now.date())}'
    # print(url_date_now)
    temperature_now=requests.get(url_date_now)
    if temperature_now.status_code==200:
        # print(temperature_now.text)
        soup_sinoptik=BeautifulSoup(temperature_now.text,"html.parser")
        temp_now = soup_sinoptik.find("p", class_="today-temp")
        print(temp_now.text)
        temperature_t=soup_sinoptik.find_all("div",class_="temperature")
        temp_min=soup_sinoptik.find("div",class_="min")
        # print(temp_min.span.string)
        temp_max = soup_sinoptik.find("div", class_="max")
        text=f'Температура в Рівному на даний момент ставновить {temp_now.string}\n' \
              f'мін:{temp_min.span.string} , макс:{temp_max.span.string}'
        return text
    else:
        return f'Помилка {temperature_now.status_code}'


#Використання агента для отримання даних про погоду за запитом з google.com.ua
def parsPogoda1():
    '''
     <div class="temperature">
      <div class="min">мін. <span>+13°</span></div>
      <div class="max">макс. <span>+18°</span></div>
    </div>
        <p class="today-temp">+15°C</p>
        <span class="wob_t TVtOme" id="wob_tm" style="display:inline">17</span>
    '''
    # Посилання на потрібну сторінку (ключові слова в google.com "погода в Рівному")
    # url="https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%A0%D1%96%D0%B2%D0%BD%D0%BE%D0%BC%D1%83&rlz=1C1OKWM_ruUA876UA876&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%A0%D1%96%D0%B2%D0%BD%D0%BE%D0%BC%D1%83&aqs=chrome..69i57j0i457j0l8.5208j1j15&sourceid=chrome&ie=UTF-8"
    url="https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D1%80%D1%96%D0%B2%D0%BD%D0%B5&rlz=1C1OKWM_ruUA876UA876&oq=%D0%BF%D0%BE%D0%B3%D0%BE&aqs=chrome.1.0i131i433i512l2j69i57j0i131i433j0i131i433i512l2j0i131i433l4.2288j1j15&sourceid=chrome&ie=UTF-8"
    headers={
        # 'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    }
    temperature_now=requests.get(url,headers=headers)
    if temperature_now.status_code==200:
        # print(temperature_now.content)
        soup=BeautifulSoup(temperature_now.text,"html.parser")
        temp_now=soup.find("span",class_="wob_t q8U8x")
        # <div class="vk_bk TylWce SGNhVe"><span class="wob_t q8U8x" id="wob_tm" style="display:inline">19</span><span class="wob_t" id="wob_ttm" style="display:none">66</span></div>
        return temp_now.string
    else:
        return f'Помилка {temperature_now.status_code}'



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://www.ukr.net/news/jekonomika.html"
    data = requests.get(url, 'html')
    # print(data.content)
    # print(data.text)
    data_text = data.text
    """
    Дістанемо всі посилання з тега a за класом "im-tl_a"
    <a href="https://metallurgprom.org/news/ukraine/8336-ceny-na-stalelitejnoe-syre-stremitelno-rastut-na-vseh-napravlenijah.html" 
    class="im-tl_a" rel="nofollow" target="_blank" data-count="85049042,48767527,3,0">
    Цены на сталелитейное сырье стремительно растут на всех направлениях</a>
    """
    soup = BeautifulSoup(data_text, "html.parser")
    # print(soup.prettify())
    # print(soup.a.b)
    href_list = soup.find_all("a", class_="im-tl_a")
    # print(href_list["href"])
    for a_imtla in href_list:
        #виведення всіх
        print(a_imtla["href"])
        #виведення контексту тега a
        print(a_imtla.string)
    #запуск функції, що отримує інформацію про погоду: температуру в Рівному
    print(parsPogoda())
    print(parsPogoda1())

