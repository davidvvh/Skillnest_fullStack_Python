from flask_app.config.mysqlconnection import connectToMySQL

class Comentario:
    DB = "schema_cinepedia"

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.usuario_id = data['usuario_id']
        self.Pelicula_id = data['Pelicula_id']
        self.author_name = data.get('author_name', 'usuario')
        self.created_at = data['created_at']

    @classmethod
    def save(cls, data):
        query = """INSERT INTO comentarios (content, usuario_id, Pelicula_id, created_at, updated_at)
                    VALUES (%(content)s, %(usuario_id)s, %(Pelicula_id)s, NOW(), NOW());"""
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_Pelicula_id(cls, data):
        """devuelve comentarios desde los más antiguos a los más recientes[cite: 1]."""
        query = """SELECT comentarios.*, usuario.first_name AS author_name 
                    FROM comentarios JOIN usuario ON comentarios.usuario_id = usuario.id 
                    WHERE comentarios.Pelicula_id = %(Pelicula_id)s 
                    ORDER BY comentarios.created_at DESC;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        comentarios = []
        if results:
            for row in results:
                comentarios.append(cls(row))
        return comentarios

    @classmethod
    def delete(cls, data):
        """permite borrar el comentario solo si pertenece al usuario que lo hizo[cite: 1]."""
        query = "DELETE FROM comentarios WHERE id = %(id)s AND usuario_id = %(usuario_id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)