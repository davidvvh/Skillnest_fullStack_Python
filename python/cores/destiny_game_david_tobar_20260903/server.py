import random
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
# Es obligatorio configurar secret_key para usar sesiones (session)
app.secret_key = "clave_secreta_destino"

# Ruta principal: muestra el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta POST: procesa los datos del formulario y los guarda en sesión
@app.route('/enviar', methods=['POST'])
def enviar():
    # Se obtienen los datos del formulario enviando la clave del 'name' en HTML
    session['nombre'] = request.form['nombre']
    session['edad'] = request.form['edad']
    session['color'] = request.form['color']
    session['animal'] = request.form['animal']
    
    # Generar predicción aleatoria (Buena suerte o mala suerte/divertida)
    predicciones = [
        "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
        "Tendrás una gran fortuna inesperada, pero ten cuidado de no gastarla toda el primer día.",
        "Un gran viaje te espera pronto, descubrirás lugares mágicos e increíbles.",
        "Ten cuidado hoy, es muy probable que te tropieces o se te caiga la comida al suelo."
    ]
    session['prediccion'] = random.choice(predicciones)
    session['numero_suerte'] = random.randint(1, 100)
    
    # Se redirige a /futuro mediante GET para evitar reenvío de formulario al recargar
    return redirect('/futuro')

# Ruta para mostrar el resultado guardado en sesión
@app.route('/futuro')
def futuro():
    # Si no hay datos en sesión, redirigimos al inicio por seguridad
    if 'nombre' not in session:
        return redirect('/')
        
    return render_template('futuro.html')

if __name__ == '__main__':
    app.run(debug=True)