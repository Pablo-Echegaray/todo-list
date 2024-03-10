from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from . import todo, auth

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
    
    # Initialize the app with the extension
    db.init_app(app)
    
    # Registrar Blueprint
    from . import todo
    app.register_blueprint(todo.bp)
    from . import auth
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

# Realizar pequeñas consultas a la DB desde Flask Shell.
# 1- Con el servidor arriba, abrir una nueva pestaña en PowerShell
# 2- Abrir shell de Flask: 
   # 2.1- Navegar hacia nuestro proyecto (cd environment\curso-flask\todo-list)
   # 2.2- Activar el entorno virtual (.\env-todo\Scripts\activate)
   # 2.3- Activar Shell python: flask --app todor shell
   # 2.4- Se activará la consola de python y nos posicionará dentro de la carpeta 'instance' donde está nuestra base de datos: Instance: environment\curso-flask\todo-list\instance
# 3- Para realizar consultas, Importar Modelo y objeto db: 
   # 3.1- Importar Modelo: from todor.models import User, Todo
   # 3.2- Importar Objeto db: from todor import db
# 4- Crear un usuario desde la terminal: user = User('Pablo', '123456')
# 5- Listar si existen usuarios (creamos una lista y recuperamos los usuarios existentes): users = User.query.all()
   # 5.1- User.query.all(): Nos devolverá una lista con todos los registros de usuarios que tengamos en la base de datos 
   # 5.2- Por ahora esta acción nos devolverá [] porque debemos insertar el usuario credo en el punto 4 en la base de datos
# 6- Para insertar un usuario en la DB usaremos el metodo session() del objeto 'db' importado en el punto 3.2
   # 6.1- db.session.add(user): el usuario se ha insertado pero aún falta aplicar estos cambios en la DB.
   # 6.2- Aplicar cambios en la DB: db.session.commit()
# 7- Reintentamos la consulta del punto 5.1 y nos traerá <User: Pablo>: users = User.query.all()   
# 8- Finalmente comprobar en 'DB Browser for SQLite (desktop app)' click derecho en la tabla 'user' > 'Mostrar datos', y podremos visualizar los datos insertados.
# 9- Crear una tarea Todo(idUser, title, descripcion): 
   # 9.1- todo1 = Todo(1, 'Curso de Flask', 'desc')
   # 9.2- todo2 = Todo(1, 'Curso de Python', 'desc')
   # 9.3- db.session.add(todo1)
   # 9.4- db.session.commit()
   # 9.5- db.session.add(todo2)
   # 9.6- db.session.commit()
   # 9.7- todos = Todo.query.all()
   # 9.8- todos: [<Todo: Curso de Flask>, <Todo: Curso de Python>]
# 10- Obtener un registro en particular Todo.query.get(id_registro):
   # 10.1- todo = Todo.query.get(2): <Todo: Curso de Python>
# 11- Salir de la terminal: exit()   

# user: pabloeche
# contraseña: hola1234