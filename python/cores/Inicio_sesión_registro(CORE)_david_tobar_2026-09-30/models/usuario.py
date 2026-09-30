from config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NOMBRE_REGEX = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]+$')

class Usuario:
    DB = 'esquema_usuarios'

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])
        return False

    @staticmethod
    def validar_registro(usuario):
        es_valido = True
        
        # Validar Nombre
        if len(usuario['nombre']) < 2 or not NOMBRE_REGEX.match(usuario['nombre']):
            flash("El nombre debe tener al menos 2 caracteres y contener solo letras.", "registro")
            es_valido = False

        # Validar Apellido
        if len(usuario['apellido']) < 2 or not NOMBRE_REGEX.match(usuario['apellido']):
            flash("El apellido debe tener al menos 2 caracteres y contener solo letras.", "registro")
            es_valido = False

        # Validar Email
        if not EMAIL_REGEX.match(usuario['email']):
            flash("Formato de correo electrónico inválido.", "registro")
            es_valido = False
        elif Usuario.get_by_email({'email': usuario['email']}):
            flash("El correo electrónico ya se encuentra registrado.", "registro")
            es_valido = False

        # Validar Contraseña (mínimo 8 caracteres, al menos 1 número y 1 mayúscula - BONUS)
        if len(usuario['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "registro")
            es_valido = False
        elif not re.search(r"[0-9]", usuario['password']) or not re.search(r"[A-Z]", usuario['password']):
            flash("La contraseña debe incluir al menos un número y una mayúscula.", "registro")
            es_valido = False

        # Validar Confirmación
        if usuario['password'] != usuario['confirm_password']:
            flash("Las contraseñas no coinciden.", "registro")
            es_valido = False

        return es_valido