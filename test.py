import requests

# Base URL
BASE = "http://127.0.0.1:5000/"

# create new video
# response = requests.put(BASE + "video/3", {"likes": 10, "name": "Jeffrey", "views": 100000})
# print(response.json())

# multiple requests (to create video)
data = [{"likes": 78, "name": "Juan", "views": 100000},
        {"likes": 10000, "name": "How to make REST API", "views": 800000},
        {"likes": 35, "name": "Jeffrey", "views": 2000}]
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

# delete video
response = requests.delete(BASE + "video/0")
print(response)

input()

# view existing video
response = requests.get(BASE + "video/2")
print(response.json())