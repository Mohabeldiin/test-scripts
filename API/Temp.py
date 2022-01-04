"""npm start"""
import requests

test_url = ''

def get():
    """Get froo API"""
    response =requests.get('http://localhost:3000/getLinks')
    test_url = response.json().get('id')
    print(response.json())

def post():
    """Post froo API"""
    Test_result = 'Pass-Test = 100 , Fail-Test = 10 , Block-Test = 0 , Total-Test = 110'
    url = 'http://localhost:3000/addcheck'
    link = {'link': 'https://www.google.com'}
    check = {'check': Test_result }
    myobj = {link, check}
    x = requests.post(url, data=myobj)
    print(x.text)

if __name__ == "__main__":
    get()
    #post()