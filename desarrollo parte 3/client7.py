import requests

URL = f'http://localhost:8000/api/v1/users/'
USER = {
    
  "username": "user100",
  "password": "123"
}

response = requests.post(URL + "login", json=USER)
if response.status_code == 200:
    print("Bievenidos maluco parece 500 pesos de cilantro")
    print(response.json())
    print(response.cookies)
    print(response.cookies.get_dict())
    print(response.cookies.get_dict().get('user_id'))
    user_id = response.cookies.get_dict().get('user_id')
    Cookies = {'user_id': user_id }
    response = requests.get(URL + "review", cookies=Cookies)
    if response.status_code == 200:
        for reviews in response.json():
            print(f"{reviews['review']} - { reviews['score']}")
    else:
        print(response.content)


