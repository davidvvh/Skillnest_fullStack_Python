from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    nombre = request.form["nombre"]
    email = request.form["email"]
    print("===================================")
    print("Información recibida")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print("===================================")
    return redirect("/mostrar_usuario")

@app.route("/mostrar_usuario")
def mostrar_usuario():
    print("Usuario redirigido")
    print(request.form)
    return render_template("mostar.html")

if __name__ == "__main__":
    app.run(debug=True)