import requests
url="https://api.telegram.org/bot5339479535:AAFr3Cc-pqZ0IKptjmdPpurV7ddnNOGyld8/"

def getUpdatesJson(url):
    response=requests.get(url+'getUpdates')
    return response.json()

def lastUpdate(data):
    # print(type(response.json()))
    return data["result"][-1]

def getChatId(update):
    return update["message"]["chat"]["id"]

def senMessage(chatId,text):
    response=requests.get(url+"sendMessage",data={"chat_id":chatId, "text":text})
    # response=requests.post(url+"sendMessage",data={"chat_id":chatId, "text":text})
    return response


chatId=getChatId(lastUpdate(getUpdatesJson(url)))
print(chatId)
senMessage(chatId,"Tell me, please, info for you!")

# while True:
#