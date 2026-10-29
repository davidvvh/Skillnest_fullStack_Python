from config.mysqlconnection import get_db


def registrar_usuario(nombre, apellido, email, password):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """INSERT INTO usuarios (nombre, apellido, email, password)
           VALUES (%s, %s, %s, %s)""",
        (nombre, apellido, email, password)
    )
    db.commit()
    cursor.close()
    db.close()


def buscar_email(email):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()
    cursor.close()
    db.close()
    return usuario


def buscar_usuario(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()
    cursor.close()
    db.close()
    return usuario
