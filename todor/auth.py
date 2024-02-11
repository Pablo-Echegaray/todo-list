from flask import Blueprint, render_template
# Con este import hemos migrado nuestros modelos a la db
from . import models

# Vistas con Blueprint.

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register')
def register():
    return render_template('auth/register.html')

@bp.route('/login')
def login():
    return render_template('auth/login.html')