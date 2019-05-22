



import requests
import json

headers = {'content-type': 'application/json'}

connection = 'http://127.0.0.1:5000/'
# filename = 'data.json'

def add():
    # date, temperature, pressure, humidity, condition, precipitation, wind, wind_speed=None
    print("Додати новий рядок")
    date = input("    Введіть дату(день-місяць-рік): ")

    print(date)

    temperature = input("    Введіть температуру(C): ")
    print(temperature)

    precipitation = input("    Введіть опади(мм): ")
    print(precipitation)

    data = {
        'date': date,
        'temperature': int(temperature),
        'precipitation': int(precipitation),
    }
    return data

def put():
    # date, temperature, pressure, humidity, condition, precipitation, wind, wind_speed=None
    temperature = input("    Введіть температуру(C): ")
    print(temperature)

    precipitation = input("    Введіть опади(мм): ")
    print(precipitation)

    data = {
        'temperature': int(temperature),
        'precipitation': int(precipitation),
    }
    return data

def UI():
    menu = None
    while menu != "6":
        print("""Меню
                1-Ввести нові дані
                2-Видалити дані
                3-Пошук за датою
                4-Вивести всі дані
                5-змінити дані
                6-Вихід
            """)
        menu = input("Введіть число: ")
        if menu == "1":
            data= add()
            r = requests.post("http://127.0.0.1:5000/tasks", data=json.dumps(data), headers=headers)
            data = r.json()
            print(data)
        if menu == "2":
            s = input("введіть date, який необідно видалити")
            r = requests.delete("http://127.0.0.1:5000/tasks/" + s)
            data = r.json()
            print(data)
        if menu == "3":
            s = input("введіть рядок для пошуку")
            r = requests.get("http://127.0.0.1:5000/tasks/"+s)
            data = r.json()
            print(data)
        if menu == "4":
            r = requests.get("http://127.0.0.1:5000/tasks")
            data = r.json()
            print(data)
        if menu == "5":
            s = input("введіть рядок для пошуку")
            data = put()
            r = requests.put("http://127.0.0.1:5000/tasks/" + s, data=json.dumps(data), headers=headers)
            data = r.json()
            print(data)

    return



try:
    entries = requests.get(connection).json()
    UI()

except requests.exceptions.ConnectionError:
    print('Connection Error, unable to connect to ' + connection)
