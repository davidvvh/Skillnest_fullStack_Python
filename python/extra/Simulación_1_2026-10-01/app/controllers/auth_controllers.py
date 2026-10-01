import re
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from app.models.user import User

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

@auth_bp.route('/', methods=['GET'])
def index():
    if 'user_id' in session:
        return redirect(url_for('book.dashboard'))
    return render_template('auth/index.html')

@auth_bp.route('/register', methods=['POST'])
def register():
    first_name = request.form.get('first_name', '').strip()
    last_name = request.form.get('last_name', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')

    errors = False

    # Validaciones del alambre de diseño (wireframe)
    if len(first_name) < 2:
        flash('El nombre debe tener al menos 2 caracteres.', 'register_error')
        errors = True
    if len(last_name) < 2:
        flash('El apellido debe tener al menos 2 caracteres.', 'register_error')
        errors = True
    if not EMAIL_REGEX.match(email):
        flash('El correo electrónico no es válido.', 'register_error')
        errors = True
    elif User.get_by_email(email):
        flash('El correo electrónico ya está registrado.', 'register_error')
        errors = True
    if len(password) < 6:
        flash('La contraseña debe tener al menos 6 caracteres.', 'register_error')
        errors = True
    if password != confirm_password:
        flash('Las contraseñas no coinciden.', 'register_error')
        errors = True

    if errors:
        return redirect(url_for('auth.index'))

    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    user_id = User.create(first_name, last_name, email, pw_hash)

    session['user_id'] = user_id
    session['user_name'] = first_name
    return redirect(url_for('book.dashboard'))

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')

    user = User.get_by_email(email)
    if user and bcrypt.check_password_hash(user['password'], password):
        session['user_id'] = user['id']
        session['user_name'] = user['first_name']
        return redirect(url_for('book.dashboard'))

    flash('Credenciales inválidas.', 'login_error')
    return redirect(url_for('auth.index'))

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.index'))