import requests
import json

get_url = "https://a5r-testing.herokuapp.com/getLink"
post_url = "https://a5r-testing.herokuapp.com/addNewlink"

#print(len(data)-1)
#print(len(data['get']))

data = {
    'link':"https://www.facebook.com"
}
requests.post(url=post_url, json=data, headers={'Content-Type': 'application/json'})

response = requests.get(get_url)
data = json.loads(response.text)
print(data['get'][-1]['link'])

#requests.post( post_url, 'link':"https://www.facebook.com")
