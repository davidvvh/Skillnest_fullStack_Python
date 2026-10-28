from flask import Blueprint, render_template, request, redirect, session, flash
from models.peluche_model import (
    obtener_peluches,
    obtener_peluche,
    nombre_existe,
    crear_peluche,
    editar_peluche,
    borrar_peluche,
    adoptar_peluche,
    sumar_visita
)

peluches = Blueprint("peluches", __name__)


def iniciar_sesion():
    return "usuario_id" in session


@peluches.route("/dashboard")
def dashboard():
    if not iniciar_sesion():
        return redirect("/")

    lista = obtener_peluches()

    return render_template(
        "dashboard.html",
        peluches=lista,
        nombre=session["nombre"],
        usuario_id=session["usuario_id"]
    )


@peluches.route("/nueva", methods=["GET", "POST"])
def nueva_donacion():
    if not iniciar_sesion():
        return redirect("/")

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        descripcion = request.form.get("descripcion", "").strip()

        if not nombre or not descripcion:
            flash("Todos los campos son obligatorios.")
            return redirect("/nueva")

        if nombre_existe(nombre):
            flash("Ya existe un peluche con ese nombre.")
            return redirect("/nueva")

        crear_peluche(nombre, descripcion, session["usuario_id"])
        flash("Peluche donado correctamente.")
        return redirect("/dashboard")

    return render_template("nueva_donacion.html")


@peluches.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_donacion(id):
    if not iniciar_sesion():
        return redirect("/")

    peluche = obtener_peluche(id)

    if not peluche:
        return redirect("/dashboard")

    if peluche["usuario_id"] != session["usuario_id"]:
        flash("No puedes editar este peluche.")
        return redirect("/dashboard")

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        descripcion = request.form.get("descripcion", "").strip()

        if not nombre or not descripcion:
            flash("Todos los campos son obligatorios.")
            return redirect(f"/editar/{id}")

        if nombre_existe(nombre, id):
            flash("Ya existe otro peluche con ese nombre.")
            return redirect(f"/editar/{id}")

        editar_peluche(id, nombre, descripcion)
        flash("Peluche actualizado correctamente.")
        return redirect("/dashboard")

    return render_template("editar_donacion.html", peluche=peluche)


@peluches.route("/borrar/<int:id>", methods=["POST"])
def borrar(id):
    if not iniciar_sesion():
        return redirect("/")

    peluche = obtener_peluche(id)

    if peluche and peluche["usuario_id"] == session["usuario_id"]:
        borrar_peluche(id)
        flash("Peluche borrado correctamente.")
    else:
        flash("No puedes borrar este peluche.")

    return redirect("/dashboard")


@peluches.route("/ver/<int:id>")
def ver_donacion(id):
    peluche = obtener_peluche(id)

    if not peluche:
        return redirect("/dashboard" if iniciar_sesion() else "/")

    sumar_visita(id)
    peluche = obtener_peluche(id)

    return render_template(
        "ver_donacion.html",
        peluche=peluche
    )


@peluches.route("/adoptar/<int:id>", methods=["POST"])
def adoptar(id):
    if not iniciar_sesion():
        return redirect("/")

    peluche = obtener_peluche(id)

    if not peluche:
        flash("El peluche no existe.")
    elif peluche["usuario_id"] == session["usuario_id"]:
        flash("No puedes adoptar tu propio peluche.")
    elif peluche["adoptado_por"] is not None:
        flash("Este peluche ya fue adoptado.")
    elif adoptar_peluche(id, session["usuario_id"]):
        flash("¡Has adoptado el peluche!")
    else:
        flash("No se pudo adoptar el peluche.")

    return redirect("/dashboard")