from flask import Blueprint

#Crear y configurar el Blueprint
my_blueprint = Blueprint('my_blueprint',
                        __name__,
                        url_prefix= '/ejemplo'  )

#crear ruta del blueprint

@my_blueprint.route('/saludo')
def saludo():
    return 'prueba blueprint'