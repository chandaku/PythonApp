import requests



def getJsonResponse():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    return jsonResponse