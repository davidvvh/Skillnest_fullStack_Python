import pymysql
from flask import current_app

def get_db_connection():
    return pymysql.connect(
        host=current_app.config['MYSQL_HOST'],
        user=current_app.config['MYSQL_USER'],
        password=current_app.config['MYSQL_PASSWORD'],
        database=current_app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )

class Book:
    @staticmethod
    def get_user_books(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT b.*, COUNT(f.user_id) AS favorites_count
            FROM books b
            LEFT JOIN favorites f ON b.id = f.book_id
            WHERE b.user_id = %s
            GROUP BY b.id
            ORDER BY b.created_at DESC
        """
        cursor.execute(query, (user_id,))
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def get_community_books(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT b.*, u.first_name AS author_user, COUNT(f.user_id) AS favorites_count
            FROM books b
            JOIN users u ON b.user_id = u.id
            LEFT JOIN favorites f ON b.id = f.book_id
            WHERE b.user_id != %s
            GROUP BY b.id
            ORDER BY b.created_at DESC
        """
        cursor.execute(query, (user_id,))
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def get_by_id(book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT b.*, u.first_name AS published_by, COUNT(f.user_id) AS favorites_count
            FROM books b
            JOIN users u ON b.user_id = u.id
            LEFT JOIN favorites f ON b.id = f.book_id
            WHERE b.id = %s
            GROUP BY b.id
        """
        cursor.execute(query, (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book

    @staticmethod
    def create(title, author, genre, publication_date, description, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO books (title, author, genre, publication_date, description, user_id)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (title, author, genre, publication_date, description, user_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update(book_id, title, author, genre, publication_date, description):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE books 
               SET title = %s, author = %s, genre = %s, publication_date = %s, description = %s
               WHERE id = %s""",
            (title, author, genre, publication_date, description, book_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def add_favorite(user_id, book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT IGNORE INTO favorites (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
        conn.commit()
        conn.close()

    @staticmethod
    def is_favorite(user_id, book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM favorites WHERE user_id = %s AND book_id = %s", (user_id, book_id))
        fav = cursor.fetchone()
        conn.close()
        return fav is not None

    @staticmethod
    def get_favorited_users(book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """SELECT u.first_name, u.last_name FROM users u
                JOIN favorites f ON u.id = f.user_id
                WHERE f.book_id = %s""",
            (book_id,)
        )
        users = cursor.fetchall()
        conn.close()
        return users

    @staticmethod
    def get_user_favorites(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT b.*, f.created_at AS fav_date
            FROM books b
            JOIN favorites f ON b.id = f.book_id
            WHERE f.user_id = %s
            ORDER BY f.created_at DESC
        """
        cursor.execute(query, (user_id,))
        books = cursor.fetchall()
        conn.close()
        return books