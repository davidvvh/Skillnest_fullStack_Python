from flask import Blueprint, render_template, request, redirect, session, flash
from models.usuario_model import registrar_usuario, buscar_email

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        accion = request.form.get("accion")

        if accion == "registro":
            nombre = request.form.get("nombre", "").strip()
            apellido = request.form.get("apellido", "").strip()
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")
            confirmar = request.form.get("confirmar", "")

            if not nombre or not apellido or not email or not password or not confirmar:
                flash("Todos los campos son obligatorios.")
                return redirect("/")

            if len(nombre) < 2 or len(apellido) < 2:
                flash("El nombre y apellido deben tener al menos 2 caracteres.")
                return redirect("/")

            if "@" not in email or "." not in email.split("@")[-1]:
                flash("El email no es válido.")
                return redirect("/")

            if password != confirmar:
                flash("Las contraseñas no coinciden.")
                return redirect("/")

            if buscar_email(email):
                flash("Ese email ya está registrado.")
                return redirect("/")

            registrar_usuario(nombre, apellido, email, password)
            flash("Cuenta creada. Ahora puedes iniciar sesión.")
            return redirect("/")

        if accion == "login":
            email = request.form.get("email", "").strip().lower()
            password = request.form.get("password", "")
            usuario = buscar_email(email)

            if usuario and usuario["password"] == password:
                session["usuario_id"] = usuario["id"]
                session["nombre"] = usuario["nombre"]
                return redirect("/dashboard")

            flash("Email o contraseña incorrectos.")
            return redirect("/")

    return render_template("index.html")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/")
