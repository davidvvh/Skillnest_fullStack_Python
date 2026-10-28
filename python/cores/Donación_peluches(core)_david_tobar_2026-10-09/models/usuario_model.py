from config.mysqlconnection import query_db

def registrar_usuario(nombre, apellido, email, password):
    db = db
    cursor = db.cursor()
    sql = """
        INSERT INTO usuarios (nombre, apellido, email, password)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (nombre, apellido, email, password))
    db.commit()

    cursor.close()
    db.close()


def buscar_email(email):
    db = db
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM usuarios WHERE email = %s",
        (email,)
    )

    usuario = cursor.fetchone()

    cursor.close()
    db.close()

    return usuario


def buscar_usuario(id):
    db = db
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM usuarios WHERE id = %s",
        (id,)
    )

    usuario = cursor.fetchone()

    cursor.close()
    db.close()

    return usuario