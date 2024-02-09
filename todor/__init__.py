from flask import Flask
from . import todo

def create_app():

    app = Flask(__name__)
    
    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev'
    )
    
    # Registrar Blueprint
    app.register_blueprint(todo.bp)
    
    @app.route('/')
    def index():
        return 'Hola Mundo'
    
    return app

# flask --app todor --debug run