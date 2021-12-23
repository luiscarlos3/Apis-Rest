from typing import List
from fastapi import HTTPException
from fastapi.security import HTTPBasicCredentials
from fastapi import Response
from fastapi import Cookie
from ..database import User
from ..schemas import UserResponseModel, reviewResponseModel
from ..schemas import UserRequestModel
from fastapi import APIRouter

router = APIRouter(prefix='/users')

@router.post('', response_model=UserResponseModel)
async def create_user(user:UserRequestModel):
    if User.select().where(User.username == user.username).exists():
        raise HTTPException(409,"No joda tu eres estupido meta un username diferente no joda ")
    has_password = User.creat_password(user.password)
    user = User.create(
        username = user.username,
        password = has_password         
    )
    return user #UserResponseModel(id=user.id, username = user.username)

@router.post('/login', response_model=UserResponseModel)
async def login(credencials:HTTPBasicCredentials, response: Response):
    user = User.select().where(User.username == credencials.username).first()
    if user is None:
        raise HTTPException(404, 'ey vale mia que el usuario no esta')
    if user.password != User.creat_password(credencials.password):
        raise HTTPException(404, 'la contraseña no es vale mia')
    response.set_cookie(key='user_id', value=user.id) # TOKEN
    return user

@router.get('/review', response_model=List[reviewResponseModel])
async def get_Reviews(user_id:int = Cookie(None)):
    user = User.select().where(User.id == user_id).first()
    if user is None:
        raise HTTPException(404, 'ey vale mia que el usuario no esta')
    return [user_review for user_review in user.reviews]
        
        
    
    