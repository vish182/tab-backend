import requests

def seperate():
    url = 'http://localhost:5555/seperate'
    myobj = {}

    x = requests.post(url, json = myobj)

    return
