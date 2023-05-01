import requests
import json
from time import  sleep
# tocken="1601733261:AAFewQtugTk9vzIHyQMa524wH20znCZqWFw"
# бот кт41
tocken="5339479535:AAFr3Cc-pqZ0IKptjmdPpurV7ddnNOGyld8"

url=f"https://api.telegram.org/bot{tocken}/"
urlFile=f"https://api.telegram.org/file/bot{tocken}/getFile?"
print(url)

def get_updates_json(request):
    response=requests.get(request+'getUpdates')
    # print(response.json())
    return response.json()

def last_update(data):
    results=data['result']
    total_updates=len(results)-1
    return results[total_updates]

def get_chat_id(update):
    chat_id=update['message']['chat']['id']
    return chat_id

# def get_message_text(update):
#     chat_id=update['message']['chat']['id']
#     return chat_id

#response BOT
def send_message(chat,text):
    parametrs={'chat_id':chat,'text':text}
    response=requests.post(url+'sendMessage',data=parametrs)
    return response

def send_photo(chat,photo):
    parametrs={'chat_id':chat,'photo':photo}
    response=requests.post(url+'sendPhoto',data=parametrs)
    return response
    # urlSend = url + 'sendPhoto'
    # answer = {'chat_id': chat_id, 'photo': photo}
    # r = requests.post(urlSend, json=answer)
    # return r.json()
    # f = open("C:\\Python37\\project\\photo\\1.jpg", 'rb')
    # send_photo(chat_id, f)

if __name__ == "__main__":
    # print(get_updates_json(url))
    # print(last_update(get_updates_json(url)))
    # print(get_chat_id(last_update(get_updates_json(url))))
    # chat_id = get_chat_id(last_update(get_updates_json(url)))
    # response=requests.post(url+'sendMessage',data={'chat_id':chat_id,'text':"Привіт, ще раз"})
    # send_message(chat_id, "Test1")
    # print(get_updates_json(url))
    if get_updates_json(url)!=None:
        update_id=last_update(get_updates_json(url))["update_id"]

        while True:
            current_id=last_update(get_updates_json(url))["update_id"]
            if update_id==current_id:
                chat_id = get_chat_id(last_update(get_updates_json(url)))
                if "text" in last_update(get_updates_json(url))["message"]:
                    result_text_updates=last_update(get_updates_json(url))["message"]["text"]
                    # print(result_text_updates)
                    send_message(chat_id,result_text_updates)
                    update_id+=1
                elif "photo" in last_update(get_updates_json(url))["message"]:
                    photo=last_update(get_updates_json(url))["message"]["photo"]

                    print(photo[-1]["file_id"])
                    # downFile=urlFile.join("file_id=",photo[-1]["file_id"])
                    # print(photo[-1])
                    fileInfo=requests.get('https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(tocken, photo[-1]["file_id"]))
                    print(fileInfo.json())
                    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(tocken, fileInfo.json()["result"]["file_path"]))
                    # print(file.n())
                    downloaded_file=file.content
                    # print(file.content)
                    f = open("D:\\photo\\3a.jpg", 'rb')
                    # send_photo(chat_id, f)

                    send_photo(chat_id,file)
                    update_id+=1
            sleep(10)
