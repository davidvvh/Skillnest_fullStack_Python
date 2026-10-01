import pymysql.cursors

class MySQLConnection:
    def get_db_connection():
        return pymysql.connect(
            host="localhost",
            user="root",
            password="1234",  # <-- Agrega tu contraseña aquí
            database="simulacion 1",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Algo salió mal:", e)
                return False
            finally:
                self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)