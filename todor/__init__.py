from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from . import todo, auth

# create the extension
db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    
    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI= 'sqlite:///todolist.db'
        
    )
    
    # Inicialize the app with the extension
    db.init_app(app)
    
    # Registrar Blueprint
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)
    
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # Create the Tables
    with app.app_context():
        db.create_all()
    
    return app

# flask --app todor --debug run
# python .\run.py
# SQLAlchemy https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#configure-the-extension
