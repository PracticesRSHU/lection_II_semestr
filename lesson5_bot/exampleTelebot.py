# import requests
#pip install requests
import telebot
#pip install pytelegrambotapi

tocken="1601733261:AAFewQtugTk9vzIHyQMa524wH20znCZqWFw"
bot = telebot.TeleBot(tocken)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "{},як справи? Надішлеш мені якесь фото?".format(message.chat.first_name))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(message.chat.id, message.text)

#Для демонстрації роботи із фото даний метод надсилає назад фото і як відповідь завантажує файл на диск
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # доступаємося до файла на сервері
    print(message.photo)
    file_info = bot.get_file(message.photo[-1].file_id)
    print(file_info)
    # бот відправляє користувачу наіслане ним фото назад
    bot.send_photo(message.chat.id, message.photo[-1].file_id)

    #завантажуємо файл із сервера із використанням методів модуля telebot
    downloaded_file = bot.download_file(file_info.file_path)
    # це еквівалентно використанню модуля requests двом командам (це якщо навіть не використовувати модулі для роботи з API телеграм):
    # 1) file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(tocken, file_info.file_path))
    # 2) downloaded_file=file.content

    #шлях до папки, наприклад, "D:/2020_2021/"+"photos/назва файлу", тому обовязково
    # потрібно створити папку photos в папці D:/2020_2021/
    src = 'D/2020_2021/' + file_info.file_path;
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Прийнято і завантажено! Фото завантажено на диск!:)")

bot.polling()