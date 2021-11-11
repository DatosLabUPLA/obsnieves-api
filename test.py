import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "videos/1", data={"likes": 10, "name": "hola", "views": 10})
print(response.json())

