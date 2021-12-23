from wsgiref.simple_server import make_server
# el parametro env es un diccionario donde se almacena informacion relavante
# con respecto a la peticion del cliente seremos capaces de conocer el protecolo htttp 
# start_response es un callball en cual recibe de manera obligatoria 2 argumentos
# el primer argumento es el status call que se le enviara el cliente 
# segundo argumento es un listado de encabezados los encabezados que el servidor envie al cliente
# esta funcion obligatoria 

HTML = """ 
 <!DOCTYPE html>
<html>
<head>
<title> Hola mundo </title>
</head>
<body>

<h1>Hola meruzca soy python </h1>
<p> En la buena </p>

</body>
</html> 
"""

def application(env, start_response):
    headers = [('Content-type', 'text/html')]
    
    start_response('200 OK', headers)
    
    return [bytes(HTML, 'utf-8')]

server = make_server('localhost', 8000, application)

server.serve_forever()

