# Este es el archivo que se ejecuta para iniciar la aplicación Flask.

from app import create_app

# Crear la aplicación Flask
app = create_app()

if __name__ == '__main__':
    # Iniciar la aplicación Flask
    app.run(debug=True)