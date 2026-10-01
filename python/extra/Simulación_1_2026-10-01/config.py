import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key_bookhub_123'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '' # Coloca tu contraseña de MySQL
    MYSQL_DB = 'bookhub_db'
    MYSQL_CURSORCLASS = 'DictCursor'