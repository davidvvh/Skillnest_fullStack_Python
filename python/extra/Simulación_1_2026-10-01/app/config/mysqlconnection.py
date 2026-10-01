import pymysql.cursors
import os

class MySQLConnection:
    def __init__(self, db='bookhub_db'):
        # Puedes cambiar estos valores por variables de entorno o valores por defecto
        self.host = os.environ.get('MYSQL_HOST', 'localhost')
        self.user = os.environ.get('MYSQL_USER', 'root')
        self.password = os.environ.get('MYSQL_PASSWORD', '')  # Tu contraseña de MySQL
        self.db = db
        self.port = int(os.environ.get('MYSQL_PORT', 3306))

        # Crear la conexión
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            port=self.port,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

    def query_db(self, query, data=None):
        """
        Ejecuta una consulta SQL.
        - Para SELECT: Retorna una lista de diccionarios (o un solo diccionario/None si es vacío).
        - Para INSERT: Retorna el ID generado (lastrowid).
        - Para UPDATE/DELETE: Retorna None o True tras hacer el commit.
        """
        with self.connection.cursor() as cursor:
            try:
                # Reemplazar %s con la data de forma segura
                cursor.execute(query, data)

                if query.lower().startswith('insert'):
                    # Retorna el id recién insertado
                    return cursor.lastrowid
                elif query.lower().startswith('select'):
                    # Retorna todos los resultados
                    result = cursor.fetchall()
                    return result
                else:
                    # Para UPDATE, DELETE, etc.
                    self.connection.commit()
            except Exception as e:
                print("Error ejecutando la consulta en la base de datos:", e)
                return False
            finally:
                self.connection.close()


def connectToMySQL(db='bookhub_db'):
    """Función de conveniencia para instanciar la conexión."""
    return MySQLConnection(db)