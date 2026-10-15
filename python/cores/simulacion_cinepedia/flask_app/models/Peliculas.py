from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class pelicula:
    DB = "schema_cinepedia"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.director = data['director']
        self.release_date = data['release_date']
        self.synopsis = data['synopsis']
        self.usuario_id = data['usuario_id']
        self.creator_name = data.get('creator_name', 'Usuario desconocido')
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """INSERT INTO Peliculas (title, director, release_date, synopsis, usuario_id, created_at, update_at)
                    VALUES(%(title)s, %(director)s, %(release_date)s, %(synopsis)s, %(usuario_id)s, NOW(), NOW());"""
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        """devolver todas las peliculas unidas con el nombre de quien las creo"""
        query = """SELECT Peliculas.*, CONCAT(usuario.first_name, ' ', usuario.last_name) AS creator_name
                    FROM Peliculas JOIN usuario ON Peliculas.usuario_id = usuario_id
                    ORDER BY Peliculas.created_at DESC;"""
        results = connectToMySQL(cls.DB).query_db(query)
        Peliculas = []
        if results:
            for row in results:
                Peliculas.append(cls(row))
        return Peliculas

    @classmethod
    def get_by_id(cls, data):
        query = """SELECT Peliculas.*, CONCAT(usuario.first_name, ' ', usuario.last_name) AS creator_name
                    FROM Peliculas JOIN usuario ON Peliculas.usuario_id = usuario.id
                    WHERE Peliculas.id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0]) if results else None

    @classmethod
    def get_by_title(cls, data):
        """usa el nombre exacto de la pelicula para buscar coincidencias"""
        query = "SELECT * FROM Peliculas WHERE title = %(title)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results[0] if results else None

    @classmethod
    def update(cls, data):
        query = """UPDATE Peliculas SET title=%(title)s, director=%(director)s,
                    release_date=%(release_date)s, synopsis=%(synopsis)s, updated_at=NOW()
                    WHERE id=%(id)s;"""
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete(cls, data):
            query = "DELETE FROM Peliculas WHERE id = %(id)s;"
            return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_movie(data, current_Pelicula_id=None):
        """Aplica las reglas descritas en el formulario de la película[cite: 1]."""
        is_valid = True

        #todos los campos de texto deben contener al menos 3 caracteres[cite: 1]
        if len(data.get('title', '').strip()) < 3:
            flash("el nombre de la película debe contener como min 3 caracteres.", "Pelicula")
            is_valid = False

        if len(data.get('director', '').strip()) < 3:
            flash("el nombre del director debe contener min 3 caracteres.", "Pelicula")
            is_valid = False

        if not data.get('release_date'):
            flash("el campo de fecha de estreno no puede estar vacío.", "Pelicula")
            is_valid = False

        if len(data.get('synopsis', '').strip()) < 3:
            flash("la sinopsis no puede estar vacía ni ser tan corta.", "Pelicula")
            is_valid = False

        # el título debe ser único en la base de datos[cite: 1]
        existing = pelicula.get_by_title({'title': data.get('title', '').strip()})
        if existing:
            # en caso de edición, se permite mantener el mismo título de la película actual
            if current_Pelicula_id is None or str(existing['id']) != str(current_Pelicula_id):
                flash("ya existe una película con este nombre", "Pelicula")
                is_valid = False

        return is_valid