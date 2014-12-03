import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    
    data = requests.get(url).text
    data = json.loads(data)
    
    return data['topartists']['artist']['rank'==1]['name']

url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&limit=1&api_key=32c501b950e032a2a0879128bc47977b&format=json'
print api_get_request(url)
