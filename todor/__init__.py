from flask import Flask

def create_app():

    app = Flask(__name__)
    
    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev'
    )
    
    @app.route('/')
    def index():
        return 'Hola Mundo'
    
    return app

# flask --app todor --debug run