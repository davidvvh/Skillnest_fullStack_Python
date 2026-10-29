import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "db_peluches")
    )


# Esta funcion tambien queda disponible para los controladores
# que la necesiten.
def query_db(query, params=()):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(query, params)
    resultado = cursor.fetchall()

    cursor.close()
    db.close()
    return resultado
