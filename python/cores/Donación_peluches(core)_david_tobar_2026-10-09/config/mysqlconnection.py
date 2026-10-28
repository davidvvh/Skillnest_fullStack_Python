import mysql.connector


def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_peluches"
    )


def query_db(query, params=()):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(query, params)
    resultado = cursor.fetchall()

    cursor.close()
    db.close()

    return resultado