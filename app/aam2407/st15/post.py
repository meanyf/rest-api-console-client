import requests
import json

# URL, на который отправляем запрос
url = "http://localhost:5000/st6/api/1"


# Данные, которые отправляем в формате JSON

data = {
    "id" : 1, # 0 для нового post
    "name": "oooooooooooooooooodgfd",
    "age": 1555552,
    "grade": "d"
}

# Заголовки, указывающие, что данные передаются в формате JSON
headers = {
    "Content-Type": "application/json"
}

# Отправка POST-запроса
response = requests.put(url, json=data)

# Печать статуса ответа
print("Статус:", response.status_code)


