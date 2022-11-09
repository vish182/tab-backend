import urllib
import urllib.request 

def download_audio(url):
    urllib.request.urlretrieve(url, "./handlers/audio/music/temp.wav")
