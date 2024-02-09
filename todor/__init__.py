from flask import Flask, render_template
from . import todo, auth

def create_app():

    app = Flask(__name__)
    
    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev'
    )
    
    # Registrar Blueprint
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)
    
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

# flask --app todor --debug run