from flask import Blueprint

# Vistas con Blueprint.

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list')
def index():
    return "Lista de tareas"