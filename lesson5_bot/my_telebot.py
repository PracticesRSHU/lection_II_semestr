import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import datetime

# tocken="1786405849:AAGDCpKmASMGRx58Ouf1y84xTwzBTo4dAmk"
tocken="5339479535:AAFr3Cc-pqZ0IKptjmdPpurV7ddnNOGyld8"
bot = telebot.TeleBot(tocken)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Ласкаво прошу до розмови!")

@bot.message_handler(commands=['help'])
def send_infoHelp(message):
	text="/sitefmi -  перехід на сайт факультету \n" \
		 "/menu - виклик меню"
	bot.send_message(message.chat.id, "Це допомога!\n"+text)

@bot.message_handler(commands=['sitefmi'])
def send_infoUrlFmi(message):
	urlFMI="http://fmi-rshu.org.ua/"
	text=f'Сайт твого факультету доступний за посиланням <a href="{urlFMI}">Сайт ФМІ</a>'
	bot.send_message(message.chat.id, text,parse_mode='html')

@bot.message_handler(content_types=['photo'])
def send_photos(message):
	print(message)
	file_info=bot.get_file(message.photo[-1].file_id)
	print(file_info)
	downloaded_file=bot.download_file(file_info.file_path)
	bot.send_photo(message.chat.id,message.photo[-1].file_id)
	src = 'D:/2020_2021/' + file_info.file_path;
	with open(src, 'wb') as new_file:
		new_file.write(downloaded_file)
	bot.reply_to(message,"Фото завантажене")

@bot.message_handler(commands=['menu'])
def send_menu(message):
	murkup=types.InlineKeyboardMarkup()
	btn1=types.InlineKeyboardButton("Погода в Рівному",callback_data="parsPogoda")
	btn2 = types.InlineKeyboardButton("Курс долара", callback_data="parsDollar")
	murkup.add(btn1,btn2)
	bot.send_message(message.chat.id,"Виберіть пункт меню:",parse_mode='html',reply_markup=murkup)

@bot.callback_query_handler(func=lambda call:True)
def callback_woker(call):
	text_msg="None"
	# print(call.data)
	# print(parsPogoda())
	if call.data=="parsPogoda":
		text_msg=parsPogoda()
	elif call.data=="parsDollar":
		text_msg = parsDollar()
	bot.send_message(call.message.chat.id, text_msg)

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
	url_date_now = f'{url}{str(date_now.date())}'
	print(url_date_now)
	temperature_now = requests.get(url_date_now)
	if temperature_now.status_code == 200:
		# print(temperature_now.content)
		soup_sinoptik = BeautifulSoup(temperature_now.text, "html.parser")
		temp_now = soup_sinoptik.find("p", class_="today-temp")
		temp_min = soup_sinoptik.find("div", class_="min")
		# print(temp_min.span.string)
		temp_max = soup_sinoptik.find("div", class_="max")
		text = f'Температура в Рівному на даний момент ставновить {temp_now.string}\n' \
			   f'мін:{temp_min.span.string} , макс:{temp_max.span.string}'
		return text


def parsDollar():
	# Посилання на потрібну сторінку (ключове слово в google.com "долар")
	DOLLAR_GRN = 'https://www.google.com/search?rlz=1C1OKWM_ruUA876UA876&sxsrf=ALeKk006L1Pl75X-7g86W7rgWPHtCLIfcQ%3A1614235575840&ei=t0c3YIDtMsaIrwSkpLeoBQ&q=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80&oq=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBQgAELEDMgUIABCxAzICCAAyBQgAELEDMgUIABDLATICCC4yBQgAELEDMgIIADICCAA6BwgjELADECc6BwgAELADEEM6BwguELADEENQwA9YwA9g2RBoAXACeACAAaEBiAGfApIBAzAuMpgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz&ved=0ahUKEwjApNOQuITvAhVGxIsKHSTSDVUQ4dUDCA0&uact=5'
	# Заголовки для передачі разом з URL. Для отримання агента в пошуковачі набираємо "мій user  agent"
	# Отрмаємо:
	# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
	# парсим сторінку
	full_page = requests.get(DOLLAR_GRN, headers=headers)
	# Разбираємо через BeautifulSoup
	soup = BeautifulSoup(full_page.content, 'html.parser')
	# Отримуєм потрібне значення
	# <span class="DFlfde SwHCTb" data-precision="2" data-value="27.946640000000002">27,95</span>
	value_dollar = soup.find("span", {"class": "DFlfde SwHCTb", "data-precision": 2})
	print(value_dollar["data-value"])
	current_converted_price = float(value_dollar.text.replace(",", "."))
	return value_dollar["data-value"]

if __name__ == '__main__':
	bot.polling()
