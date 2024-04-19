import requests

Base = "http://127.0.0.1:5000/"
response = requests.put(Base + "video/1", data={"likes": 100, "name": "Gangs of Wasseypur", "views": 10000})
print(response.json())
input()

# response=requests.get(Base+"video/1")
# # response=requests.delete(Base+"video/1")
# print(response)

# Send a PATCH request to update the video with ID 1
response = requests.patch(Base + "video/1", data={"name": "Gangs Of Wasseypur 3"})
print(response.json())

# Send a GET request to retrieve the updated video
response = requests.get(Base + "video/1")
print(response.json())