import requests

def getChords(filename):
    url = 'http://localhost:6000/getChords'
    myobj = {'path': str(filename)}

    x = requests.post(url, json = myobj)

    return x.text
