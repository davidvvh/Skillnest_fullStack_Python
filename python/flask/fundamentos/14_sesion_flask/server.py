from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "una-clave-secreta"


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
    session["nombre_usuario"] = nombre
    session["email_usuario"] = email

    return redirect("/mostrar_usuario")


@app.route("/mostrar_usuario")
def mostrar_usuario():
    nombre = session["nombre_usuario"]
    email = session["email_usuario"]
    print("===================================")
    print("Usuario redirigido")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print("===================================")
    return render_template("mostrar.html")

if __name__ == "__main__":
    app.run(debug=True)