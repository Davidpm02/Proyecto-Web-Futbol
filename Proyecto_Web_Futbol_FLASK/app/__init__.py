from flask import Flask

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)

    # Configuraciones de la aplicación
    app.config['SECRET_KEY'] = 'clave_secreta'

    # Registrar las rutas de la aplicación
    from .routes import main
    app.register_blueprint(main)

    return app