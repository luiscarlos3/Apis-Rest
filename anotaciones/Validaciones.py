from pydantic import BaseModel
from typing import Optional
from pydantic import ValidationError
from pydantic import validator

class User(BaseModel):
    # todos son requeridos en la clase
    username:str
    password:str
    correo:str
    repeat_password:str
    edad:Optional[int] = None
    
    @validator('username')# por default optional     
    
    def username_validation_lenght(cls,username):        
        # reglas de negocio
        if len(username) < 3:
            raise ValueError('Tu si eres es menor de 3 caracteres no joda pelado maco')
        if len(username) > 50: 
            raise ValueError('Tu si eres es mayor de 50 caracteres no joda pelado maco')
        return username
    
    @validator('repeat_password')
    def repeat_password_validation(cls, repeat_password, values):
        if 'password' in values and repeat_password != values['password']:
            raise ValidationError("las contraseñas son diferentes")
        return repeat_password

try:
    user1 = User(username='cody', password='123', correo='luis@gmail.com', repeat_password='123', edad=30)
    print(user1)
except ValidationError as E:
    print(E.json())
        


