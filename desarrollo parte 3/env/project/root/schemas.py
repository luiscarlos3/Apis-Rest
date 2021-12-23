from typing import Any
from pydantic import BaseModel
from pydantic import validator
from pydantic.utils import GetterDict
from typing import Any
from peewee import ModelSelect

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res
class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
# --------- User ------------------------       
class UserRequestModel(BaseModel):
    username:str
    password:str
    
    @validator('username')
    def username_validator(cls, username):
        if len(username)< 3 or len(username) > 50:
            raise ValueError("No joda pelado maco tienes que meter username correcto ")
        return username

        
class UserResponseModel(ResponseModel):
    id:int
    username:str 
    
# --------- Movie -------------
class MovieResponseModel(ResponseModel):
    id:int
    title:str 
    
# --------- Reseña ------------------------
class ReviewValidator():
    @validator('score')
    def score_validation(cls, score):
        if score < 1 or score > 5:
            raise ValueError('no joda pelado tu si eres muy @#$!&# meta los rangos de 1 a 5 no me joda ')
        return score
          
class ReviewRequestModel(BaseModel, ReviewValidator):
    user_id : int
    movie_id : int
    review: str
    score : int
    


class reviewResponseModel(ResponseModel):
    id:int
    movie: MovieResponseModel
    review:str
    score:int
    
class ReviewRequestPutModel(BaseModel, ReviewValidator):
    review:str
    score:int

    
    