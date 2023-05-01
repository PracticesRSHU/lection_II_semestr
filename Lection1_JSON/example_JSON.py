import json
# опишемо об'єкт типу JSON
menu = {
    "hotel": {
        "roomnumber": "101-137",
        "items": {
            "single room": "$42.60",
            "restaurant": "$24.45"
        }
    },
    "campsite": {
        "roomnumber": "201-265",
        "items": {
            "internet access": "$3.62"
        }
    },
    "hostel": {
        "roomnumber": "301-312",
        "items": {
            "room service": "$1.69"
        }
    }
}

# Закодуємо структуру даних (menu) в рядок JSON  (menu_json) за допомогою функції dumps():
menu_json = json.dumps(menu)
print("menu_structura in menu_json --> ", menu_json)
print(type(menu_json))
print(60*'-')
# перетворимо рядок JSON menu_json назад у структуру даних (menu2) за допомогою функції loads():
menu2 = json.loads(menu_json)
print("menu_json in menu_structure --> ", menu2)
print(type(menu2))

