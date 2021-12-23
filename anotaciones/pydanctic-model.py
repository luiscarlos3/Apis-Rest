from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    # todos son requeridos en la clase
    username:str
    password:str
    correo:str
    edad:Optional[int] = None # por default optional 
    
user1 = User(username='luis123', password='123', correo='luis@gmail.com')

print(user1)