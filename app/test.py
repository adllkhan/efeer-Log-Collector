import requests


res = requests.get("http://localhost:8000/logs")


print(res.json())
