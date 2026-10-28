from config.mysqlconnection import get_db


def obtener_peluches():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    sql = """
        SELECT peluches.*, usuarios.nombre AS donador,
        adoptante.nombre AS adoptado_por
        FROM peluches
        JOIN usuarios ON peluches.usuario_id = usuarios.id
        LEFT JOIN usuarios AS adoptante
        ON peluches.adoptado_por = adoptante.id
        ORDER BY peluches.id DESC
    """

    cursor.execute(sql)
    peluches = cursor.fetchall()

    cursor.close()
    db.close()

    return peluches


def obtener_peluche(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    sql = """
        SELECT peluches.*, usuarios.nombre AS donador,
        adoptante.nombre AS adoptado_por
        FROM peluches
        JOIN usuarios ON peluches.usuario_id = usuarios.id
        LEFT JOIN usuarios AS adoptante
        ON peluches.adoptado_por = adoptante.id
        WHERE peluches.id = %s
    """

    cursor.execute(sql, (id,))
    peluche = cursor.fetchone()

    cursor.close()
    db.close()

    return peluche


def nombre_existe(nombre, excluir_id=None):
    db = get_db()
    cursor = db.cursor()

    if excluir_id is None:
        cursor.execute(
            "SELECT id FROM peluches WHERE LOWER(nombre) = LOWER(%s)",
            (nombre,)
        )
    else:
        cursor.execute(
            """SELECT id FROM peluches
                WHERE LOWER(nombre) = LOWER(%s) AND id != %s""",
            (nombre, excluir_id)
        )

    existe = cursor.fetchone() is not None

    cursor.close()
    db.close()

    return existe


def crear_peluche(nombre, descripcion, usuario_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """INSERT INTO peluches (nombre, descripcion, usuario_id)
            VALUES (%s, %s, %s)""",
        (nombre, descripcion, usuario_id)
    )

    db.commit()
    cursor.close()
    db.close()


def editar_peluche(id, nombre, descripcion):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """UPDATE peluches
            SET nombre = %s, descripcion = %s
            WHERE id = %s""",
        (nombre, descripcion, id)
    )

    db.commit()
    cursor.close()
    db.close()


def borrar_peluche(id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM peluches WHERE id = %s",
        (id,)
    )

    db.commit()
    cursor.close()
    db.close()


def adoptar_peluche(id, usuario_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """UPDATE peluches SET adoptado_por = %s
            WHERE id = %s AND adoptado_por IS NULL""",
        (usuario_id, id)
    )

    db.commit()
    actualizado = cursor.rowcount > 0

    cursor.close()
    db.close()

    return actualizado


def sumar_visita(id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """UPDATE peluches SET visitas = visitas + 1
            WHERE id = %s""",
        (id,)
    )

    db.commit()
    cursor.close()
    db.close()