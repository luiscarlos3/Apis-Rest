import requests

URL = 'http://localhost:8000/api/v1/users'
REQUIRED = {
  "username": "unad",
  "password": "123"
}
response = requests.post(URL, json=REQUIRED)
if response.status_code == 200:
    print("Usuario creado")
    print(response.json()['id'])
else:
    print(response.content)