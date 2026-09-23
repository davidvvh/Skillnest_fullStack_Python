# ==========================================================
# ADIVINA EL NÚMERO
# Juego desarrollado con Flask
# ==========================================================

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)
import random

app = Flask(__name__)

# Clave secreta necesaria para manejar variables de sesión
app.secret_key = "clave-secreta-adivina-numero"

@app.route("/")
def index():
    """
    Ruta principal del juego.
    Inicializa los valores de la sesión si no existen y renderiza la plantilla.
    """
    if "numero_secreto" not in session:
        session["numero_secreto"] = random.randint(1, 10)

    if "intentos" not in session:
        session["intentos"] = 0

    if "mensaje" not in session:
        session["mensaje"] = "Adivina un número entre 1 y 10."

    if "resultado" not in session:
        session["resultado"] = ""

    return render_template(
        "index.html",
        mensaje=session["mensaje"],
        resultado=session["resultado"],
        intentos=session["intentos"]
    )

@app.route("/adivinar", methods=["POST"])
def adivinar():
    """
    Procesa el formulario enviando un número mediante POST.
    Compara el número contra el número secreto de la sesión.
    """
    numero = int(request.form["numero"])
    numero_secreto = session["numero_secreto"]

    session["intentos"] += 1

    if numero < numero_secreto:
        session["mensaje"] = f"El número secreto es mayor que {numero}."
        session["resultado"] = "mayor"
    elif numero > numero_secreto:
        session["mensaje"] = f"El número secreto es menor que {numero}."
        session["resultado"] = "menor"
    else:
        session["mensaje"] = f"¡Correcto! El número secreto era {numero_secreto}."
        session["resultado"] = "correcto"

    # Patrón POST -> Redirect -> GET
    return redirect(url_for("index"))

@app.route("/reiniciar")
def reiniciar():
    """
    Limpia la sesión para reiniciar las variables y redirige al inicio.
    """
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)