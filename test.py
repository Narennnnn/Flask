import requests

Base = "http://127.0.0.1:5000/"
# response = requests.put(Base + "video/1", data={"likes": "100k", "name": "Gangs of Wasseypur", "views": "90Million"})
# print(response.json())
# input()

response=requests.get(Base+"video/2")
print(response.json())