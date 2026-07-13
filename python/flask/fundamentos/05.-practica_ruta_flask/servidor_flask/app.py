#05.-practica
from flask import Flask
app = Flask(__name__)

# Ruta raíz - Página de inicio
@app.route("/")
def inicio():
    return "<h1>¡Bienvenido a nuestro servidor flask!</h1>"
# Ruta genérica para explorar enrutamiento
@app.route("/explorar")
def explorar():
    return "¿Buscas una ruta especifica?¡Prueba las diversas y diferentes direcciones!"

# Rutas dinámicas para personalización
@app.route("/perfil/<nombre>")
def perfil(nombre):
    return f"Bienvenido seas {nombre} a tu perfil personalizado en nuestra app"

# Ruta que repite un mensaje varias veces
@app.route("/repite/<int:veces>/<mensaje>")
def repite(veces, mensaje):
    return f"repite despues de mi: {mensaje} " * veces

# BONUS: Página de error personalizada si el usuario ingresa una ruta inexistente
@app.route("/error")
def error():
    return "¡lo sentimos! no se encontro la pagina solicitada, intente nuevamente con una ruta valida"

# Ejecuta el servidor
if __name__ == "__main__":
    app.run(debug=True)