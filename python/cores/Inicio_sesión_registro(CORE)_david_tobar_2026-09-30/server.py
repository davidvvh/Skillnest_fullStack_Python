from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from models.usuario import Usuario

app = Flask(__name__)
app.secret_key = "clave_secreta_para_sesiones"
bcrypt = Bcrypt(app)

# Vista principal (Registro e Inicio de Sesión)
@app.route('/')
def index():
    if 'usuario_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

# Procesar Registro
@app.route('/registro', methods=['POST'])
def registro():
    if not Usuario.validar_registro(request.form):
        return redirect('/')

    password_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": password_hash
    }

    usuario_id = Usuario.save(data)
    session['usuario_id'] = usuario_id
    return redirect('/dashboard')

# Procesar Inicio de Sesión
@app.route('/login', methods=['POST'])
def login():
    data = {"email": request.form['email']}
    usuario_en_db = Usuario.get_by_email(data)

    if not usuario_en_db:
        flash("Email o contraseña no válidos.", "login")
        return redirect('/')

    if not bcrypt.check_password_hash(usuario_en_db.password, request.form['password']):
        flash("Email o contraseña no válidos.", "login")
        return redirect('/')

    session['usuario_id'] = usuario_en_db.id
    return redirect('/dashboard')

# Vista del Dashboard / Éxito
@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')

    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    return render_template('dashboard.html', usuario=usuario)

# Cierre de Sesión
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)