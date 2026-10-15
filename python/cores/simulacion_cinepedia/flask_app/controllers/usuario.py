from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.usuario import usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect('/cine')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not usuario.validate_register(request.form):
        session['reg_data'] = request.form
        return redirect('/')

    # Cifrado de contraseña mediante Bcrypt
    hashed_password = bcrypt.generate_password_hash(request.form['password'])

    usuario_data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": hashed_password
    }

    usuario_id = usuario.save(usuario_data)
    session['usuario_id'] = usuario_id
    session['first_name'] = request.form['first_name']
    session.pop('reg_data', None)

    return redirect('/cine')

@app.route('/login', methods=['POST'])
def login():
    usuario = usuario.get_by_email({'email': request.form.get('email', '')})

    # Verificación y comparación de correo del hash de la contraseña[cite: 1]
    if not usuario or not bcrypt.check_password_hash(usuario.password, request.form.get('password', '')):
        flash("Credenciales inválidas. Verifique el correo y contraseña.", "login")
        return redirect('/')

    session['usuario_id'] = usuario.id
    session['first_name'] = usuario.first_name
    return redirect('/cine')

@app.route('/logout')
def logout():
    """cierra la sesión y redirige al usuario a la página de login[cite: 1]."""
    session.clear()
    return redirect('/')