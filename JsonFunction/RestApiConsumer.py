import requests


def getJsonResponse():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    return jsonResponse


def postRequest():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    feed = {"userId": 11, "title": "Buy milk", "completed": False}
    response = requests.post(api_url, json=feed)
    return response.json()

def putRequest():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    feed = {"userId": 1, "title": "Buy milk", "completed": True}
    response = requests.put(api_url, json=feed)
    return response.json()

#print(postRequest())
#print(getJsonResponse())
print(putRequest())
