# Este archivo contiene el código que define las rutas y controladores para la aplicación.

from flask import Blueprint

# Crear un objeto Blueprint para las rutas
main = Blueprint('main', __name__)

# Definir una ruta
@main.route('/')
def index():
    return '¡Hola, mundo!'

# Definir otra ruta
@main.route('/about')
def about():
    return 'Acerca de nosotros'

# Agregar más rutas aquí...