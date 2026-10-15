from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

#validacion de correos de expresion regular y sintaxis estandar
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class usuario:
    DB = "schema_cinepedia"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        """ayuda a insertar un nuevo registro de usuario"""
        query = """INSERT INTO usuario (first_name, last_name, email, password, created_at, updated_at)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"""
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        """usa el correo para buscar a un usuario para validaciones de login o por su unicidad"""
        query = "SELECT * FROM usuario WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len (result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        """usa el id para obtener a un usuario para una vista personalizada"""
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if not result:
            return False
        return cls(result[0])

    @staticmethod
    def validate_register(data):
        """aplica reglas de negocio especificas en los wireframes[cite: 1]"""
        is_valid = True

        #valida la longitud del nombre y apellido (min 2 caracteres)[cite: 1]
        if len(data.get('first_name', '').strip()) < 2:
            flash("el nombre debe tener como minimo 2 caracteres", "register")
            is_valid = False

        if len(data.get('last_name', '').strip()) < 2:
            flash("el apellido debe tener como minimo 2 caracteres", "register")
            is_valid = False

        #formato correcto de e-mail valido[cite: 1]
        if not EMAIL_REGEX.match(data.get('email', '')):
            pass