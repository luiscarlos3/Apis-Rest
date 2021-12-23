from fastapi import FastAPI
from fastapi import APIRouter

from .database import database as conexion




from .routers import user_router
from .routers import review_router

app = FastAPI(title='proyecto para reseñar peliculas', description='este proyecto seremos capaces de reseñar peliculas', version='1')

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(review_router)

app.include_router(api_v1)
@app.on_event('startup')
def startup():
    if conexion.is_closed():
        conexion.connect()
        #print('Conectado a la base de datos')
    print("El servidor iniciando")
    #conexion.create_tables([User, Movie, UserReview])

@app.on_event('shutdown')
def shutdown():
    if not conexion.is_closed():
        conexion.close()
    print("Close")
    
@app.get('/')
async def index():
    return 'Hola mundo este un servidor en fast api'

@app.get('/about')
async def about():
    return 'estamos en about'





    