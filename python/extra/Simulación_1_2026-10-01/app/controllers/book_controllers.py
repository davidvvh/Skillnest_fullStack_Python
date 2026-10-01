from datetime import datetime
from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.book import Book

book_bp = Blueprint('book', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor inicia sesión para acceder.', 'login_error')
            return redirect(url_for('auth.index'))
        return f(*args, **kwargs)
    return decorated_function

@book_bp.route('/libros')
@login_required
def dashboard():
    user_id = session['user_id']
    my_books = Book.get_user_books(user_id)
    community_books = Book.get_community_books(user_id)
    return render_template('books/index.html', my_books=my_books, community_books=community_books)

@book_bp.route('/libros/nuevo', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        genre = request.form.get('genre', '').strip()
        publication_date = request.form.get('publication_date', '').strip()
        description = request.form.get('description', '').strip()

        errors = False

        if not title or len(title) < 2:
            flash('El título debe tener al menos 2 caracteres.', 'book_error')
            errors = True
        if not author:
            flash('El autor es obligatorio.', 'book_error')
            errors = True
        if not genre:
            flash('Debes seleccionar un género.', 'book_error')
            errors = True
        if not publication_date:
            flash('La fecha de publicación es obligatoria.', 'book_error')
            errors = True
        else:
            try:
                pub_date = datetime.strptime(publication_date, '%Y-%m-%d').date()
                if pub_date > datetime.now().date():
                    flash('La fecha de publicación no puede ser en el futuro.', 'book_error')
                    errors = True
            except ValueError:
                flash('Formato de fecha inválido.', 'book_error')
                errors = True

        if len(description) < 10:
            flash('La descripción debe tener al menos 10 caracteres.', 'book_error')
            errors = True

        if errors:
            return redirect(url_for('book.create'))

        Book.create(title, author, genre, publication_date, description, session['user_id'])
        return redirect(url_for('book.dashboard'))

    return render_template('books/create.html')

@book_bp.route('/libros/<int:book_id>')
@login_required
def detail(book_id):
    book = Book.get_by_id(book_id)
    if not book:
        flash('Libro no encontrado.', 'dashboard_error')
        return redirect(url_for('book.dashboard'))

    is_fav = Book.is_favorite(session['user_id'], book_id)
    fav_users = Book.get_favorited_users(book_id)

    return render_template('books/detail.html', book=book, is_fav=is_fav, fav_users=fav_users)

@book_bp.route('/libros/editar/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit(book_id):
    book = Book.get_by_id(book_id)
    if not book:
        flash('Libro no encontrado.', 'dashboard_error')
        return redirect(url_for('book.dashboard'))

    # Protección de propiedad de registro
    if book['user_id'] != session['user_id']:
        flash('No tienes permisos para modificar este libro.', 'dashboard_error')
        return redirect(url_for('book.dashboard'))

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        genre = request.form.get('genre', '').strip()
        publication_date = request.form.get('publication_date', '').strip()
        description = request.form.get('description', '').strip()

        errors = False

        if not title or len(title) < 2:
            flash('El título debe tener al menos 2 caracteres.', 'book_error')
            errors = True
        if not author:
            flash('El autor es obligatorio.', 'book_error')
            errors = True
        if not genre:
            flash('Debes seleccionar un género.', 'book_error')
            errors = True
        if not publication_date:
            flash('La fecha de publicación es obligatoria.', 'book_error')
            errors = True
        else:
            try:
                pub_date = datetime.strptime(publication_date, '%Y-%m-%d').date()
                if pub_date > datetime.now().date():
                    flash('La fecha de publicación no puede ser en el futuro.', 'book_error')
                    errors = True
            except ValueError:
                flash('Formato de fecha inválido.', 'book_error')
                errors = True

        if len(description) < 10:
            flash('La descripción debe tener al menos 10 caracteres.', 'book_error')
            errors = True

        if errors:
            return redirect(url_for('book.edit', book_id=book_id))

        Book.update(book_id, title, author, genre, publication_date, description)
        return redirect(url_for('book.dashboard'))

    return render_template('books/edit.html', book=book)

@book_bp.route('/libros/eliminar/<int:book_id>', methods=['POST'])
@login_required
def delete(book_id):
    book = Book.get_by_id(book_id)
    if book and book['user_id'] == session['user_id']:
        Book.delete(book_id)
    else:
        flash('No tienes permiso para eliminar este libro.', 'dashboard_error')
    return redirect(url_for('book.dashboard'))

@book_bp.route('/libros/favorito/<int:book_id>', methods=['POST'])
@login_required
def add_favorite(book_id):
    Book.add_favorite(session['user_id'], book_id)
    return redirect(url_for('book.detail', book_id=book_id))

@book_bp.route('/favoritos')
@login_required
def favorites():
    fav_books = Book.get_user_favorites(session['user_id'])
    return render_template('books/favorites.html', books=fav_books)