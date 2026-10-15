from flask import request, redirect, session, flash
from flask_app import app
from flask_app.models.comentarios import Comentario
from flask_app.models.Peliculas import pelicula

@app.route('/cine/comentar', methods=['POST'])
def añadir_comentario():
    if 'usuario_id' not in session:
        return redirect('/')

    Peliculas_id = request.form.get('Peliculas_id')
    Peliculas = pelicula.get_by_id({'id': Peliculas_id})

    #un usuario no puede comentar su propia película[cite: 1]
    if Peliculas and Peliculas.usuario_id == session['usuario_id']:
        flash("No tienes permitido comentar tu propia publicación.", "comentar_error")
        return redirect(f'/cine/{Peliculas_id}')

    content = request.form.get('content', '').strip()
    if len(content) > 0:
        data = {
            "content": content,
            "usuario_id": session['usuario_id'],
            "Peliculas_id": Peliculas_id
        }
        Comentario.save(data)

    return redirect(f'/cine/{Peliculas_id}')

@app.route('/cine/comentario/eliminar/<int:comentarios_id>/<int:Peliculas_id>')
def borrar_comentario(comentarios_id, Peliculas_id):
    if 'usuario_id' not in session:
        return redirect('/')

    Comentario.delete({
        'id': comentarios_id,
        'usuario_id': session['usuario_id']
    })

    return redirect(f'/cine/{Peliculas_id}')