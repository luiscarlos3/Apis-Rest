import requests
id = 3
URL = f'http://localhost:8000/api/v1/reviews/{id}'

response = requests.delete(URL)
if response.status_code == 200:
    print("Se Elimino esa jodida")
    print(response.json())

