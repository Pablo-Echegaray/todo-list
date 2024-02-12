from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
# Módulo 'session' nos ayudará en la parte de inicio de sesión, guardando el usuario que ha iniciado una sesión para saber si un usuario ha o no iniciado una sesión.
# Object 'g' se utiliza para guardar cualquier valor. Va a estar presente en todas partes de nuestra aplicación. Se utiliza para almacenar algún tipo de valor como cookies por ejemplo.
from werkzeug.security import generate_password_hash, check_password_hash
# Con este import hemos migrado nuestros modelos a la db
#from . import models
from .models import User
from todor import db

# Vistas con Blueprint.

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods = ('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User(username, generate_password_hash(password))
        error = None
        user_name = User.query.filter_by(username = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya está registrado.'
        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        error = None
        # Validar datos
        user = User.query.filter_by(username = username).first()
        if user == None:
            error = 'Nombre de usuario incorrecto.'
        elif not check_password_hash(user.password, password):
            error = 'Contraseña incorrecta.'
            
        # Iniciar sesión
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('todo.index'))
        
        flash(error)
    return render_template('auth/login.html')

# Este decorador de bp hace que esta función (función que verifica si alguien ha iniciado o no sesión) se ejecute primero en cada petición.
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)
        
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))  