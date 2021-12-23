import requests
id = 3
URL = f'http://localhost:8000/api/v1/reviews/{id}'
REVIEW = {
           "review": "que pelicula tan mala en la vida ni fuera la unica ",
           "score": 1}
response = requests.put(URL,json=REVIEW)
if response.status_code == 200:
    print("Se actualio esa jodida")
    print(response.json())

