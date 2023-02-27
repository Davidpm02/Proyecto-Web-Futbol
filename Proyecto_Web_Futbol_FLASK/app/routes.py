# Este archivo contiene el código que define las rutas y controladores para la aplicación.

from flask import Blueprint
from flask import render_template

# Crear un objeto Blueprint para las rutas
main = Blueprint('main', __name__)

# Definir una ruta
@main.route('/')
def index():
    return render_template('index.html')

# Definir otra ruta
@main.route('/about')
def about():
    return 'Acerca de nosotros'

# Agregar más rutas aquí...


#Se ha creado un objeto Blueprint llamado main que se utilizará para agrupar las rutas de la aplicación. 
# Luego, se definen dos rutas utilizando el decorador @main.route(). 