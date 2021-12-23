from wsgiref.simple_server import make_server
from jinja2 import Environment, environment
from jinja2 import FileSystemLoader
# el parametro env es un diccionario donde se almacena informacion relavante
# con respecto a la peticion del cliente seremos capaces de conocer el protecolo htttp 
# start_response es un callball en cual recibe de manera obligatoria 2 argumentos
# el primer argumento es el status call que se le enviara el cliente 
# segundo argumento es un listado de encabezados los encabezados que el servidor envie al cliente
# esta funcion obligatoria 


def application(env, start_response):
    headers = [('Content-type', 'text/html')]
    
    start_response('200 OK', headers)
    env = Environment(loader=FileSystemLoader('template'))
    template = env.get_template('index.html')
    HTML = template.render({        
        'nombre': 'pagina web',
        'titulo':'pagina web en python',
        'mensaje':'mi primera pagina web en vaina hoober'
    })
    
    return [bytes(HTML,'utf-8')]

server = make_server('localhost', 8000, application)

server.serve_forever()

