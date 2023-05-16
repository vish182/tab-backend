import requests

def seperate(start, end):
    url = 'http://localhost:5555/seperate'
    myobj = {'start': start, 'end': end}

    x = requests.post(url, json = myobj)

    return x.text
