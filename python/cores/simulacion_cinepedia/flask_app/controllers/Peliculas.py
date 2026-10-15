from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.Peliculas import pelicula
from flask_app.models.comentarios import Comentario

@app.route('/cine')
def dashboard():
    """Restringe el acceso si no hay una sesión activa[cite: 1]."""
    if 'usuario_id' not in session:
        return redirect('/')

    Peliculas = pelicula.get_all()
    return render_template('dashboard.html', Peliculas=Peliculas)

@app.route('/cine/nueva')
def nueva_Pelicula():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('nueva_pelicula.html')

@app.route('/cine/crear', methods=['POST'])
def crear_Pelicula():
    if 'usuario_id' not in session:
        return redirect('/')

    if not pelicula.validar_Pelicula(request.form):
        #mantiene los valores ingresados en la sesión temporal para no borrarlos[cite: 1]
        session['form_data'] = request.form
        return redirect('/cine/nueva')

    Peliculas_data = {
        "title": request.form['title'],
        "director": request.form['director'],
        "release_date": request.form['release_date'],
        "synopsis": request.form['synopsis'],
        "usuario_id": session['usuario_id']
    }

    pelicula.save(Peliculas_data)
    session.pop('form_data', None)
    return redirect('/cine')

@app.route('/cine/<int:id>')
def mostrar_pelicula(id):
    if 'usuario_id' not in session:
        return redirect('/')

    Peliculas = pelicula.get_by_id({'id': id})
    if not Peliculas:
        return redirect('/cine')

    comentarios = Comentario.get_by_Pelicula_id({'Pelicula_id': id})
    return render_template('mostrar_pelicula.html', Peliculas=Peliculas, comentarios=comentarios)

@app.route('/cine/editar/<int:id>')
def editar_Pelicula(id):
    if 'usuario_id' not in session:
        return redirect('/')

    Peliculas = pelicula.get_by_id({'id': id})
    # Solamente el autor puede modificar su publicación[cite: 1]
    if not Peliculas or Peliculas.usuario_id != session['usuario_id']:
        return redirect('/cine')

    return render_template('editar_pelicula.html', Peliculas=Peliculas)

@app.route('/cine/actualizar/<int:id>', methods=['POST'])
def actualizar_Pelicula(id):
    if 'usuario_id' not in session:
        return redirect('/')

    Peliculas = pelicula.get_by_id({'id': id})
    if not Peliculas or Peliculas.usuario_id != session['usuario_id']:
        return redirect('/cine')

    if not pelicula.validar_Pelicula(request.form, current_Pelicula_id=id):
        return redirect(f'/cine/editar/{id}')

    data = {
        "id": id,
        "title": request.form['title'],
        "director": request.form['director'],
        "release_date": request.form['release_date'],
        "synopsis": request.form['synopsis']
    }
    pelicula.update(data)
    return redirect('/cine')

@app.route('/cine/eliminar/<int:id>')
def borrar_Pelicula(id):
    if 'usuario_id' not in session:
        return redirect('/')

    Peliculas = pelicula.get_by_id({'id': id})
    if Peliculas and Peliculas.usuario_id == session['usuario_id']:
        pelicula.delete({'id': id})

    return redirect('/cine')