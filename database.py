import sqlite3
from datetime import datetime

db_name = "database/security.db"


# Connect to database
def connect_db():

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        print("Connected successfully")
        return conn, cursor

    except sqlite3.Error as e:
        print("Database connection error")
        print(e)
        return None, None


# Create database tables
def create_tables():

    conn, cursor = connect_db()

    if conn is None or cursor is None:
        return

    try:

        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)

        # History table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS history(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                tool_name TEXT NOT NULL,
                result TEXT NOT NULL,
                datetime TEXT NOT NULL
            )
        """)

        # File integrity table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS file_integrity(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                file_path TEXT NOT NULL,
                file_hash TEXT NOT NULL,
                datetime TEXT NOT NULL,
                UNIQUE(user_id, file_path)
            )
        """)

        conn.commit()

    except sqlite3.Error as e:

        print(f"Error creating tables: {e}")

    finally:

        conn.close()
        print("Database connection closed after creating tables.")


# Insert user
def insert_user(username, email, password):

    conn, cursor = connect_db()

    if conn is None or cursor is None:
        return False

    try:

        cursor.execute(
            """
            INSERT INTO users(username, email, password)
            VALUES (?, ?, ?)
            """,
            (username, email, password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:

        return False

    except sqlite3.Error as e:

        print(e)
        return False

    finally:

        conn.close()


# Login user
def login_user(username):

    conn, cursor = connect_db()

    if conn is None or cursor is None:
        return None

    try:

        cursor.execute(
            """
            SELECT * FROM users
            WHERE username = ?
            """,
            (username,)
        )

        user = cursor.fetchone()
        return user

    except sqlite3.Error as e:

        print(e)
        return None

    finally:

        conn.close()


# Save history
def save_history(user_id, tool_name, result):

    conn, cursor = connect_db()

    if conn is None or cursor is None:
        return False

    try:

        current_datetime = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        cursor.execute(
            """
            INSERT INTO history(
                user_id,
                tool_name,
                result,
                datetime
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                user_id,
                tool_name,
                result,
                current_datetime
            )
        )

        conn.commit()
        return True

    except sqlite3.Error as e:

        print(e)
        return False

    finally:

        conn.close()


# Get history
def get_history(user_id):

    conn, cursor = connect_db()

    if conn is None or cursor is None:
        return []

    try:

        cursor.execute(
            """
            SELECT tool_name, result, datetime
            FROM history
            WHERE user_id = ?
            ORDER BY id DESC
            """,
            (user_id,)
        )

        history = cursor.fetchall()
        return history

    except sqlite3.Error as e:

        print(e)
        return []

    finally:

        conn.close()


# Save or update file integrity hash
def save_file_hash(user_id, file_path, file_hash):

    conn, cursor = connect_db()

    if conn is None or cursor is None:
        return False

    try:

        current_datetime = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        cursor.execute(
            """
            SELECT id
            FROM file_integrity
            WHERE user_id = ? AND file_path = ?
            """,
            (user_id, file_path)
        )

        existing_file = cursor.fetchone()

        if existing_file:

            cursor.execute(
                """
                UPDATE file_integrity
                SET file_hash = ?, datetime = ?
                WHERE user_id = ? AND file_path = ?
                """,
                (
                    file_hash,
                    current_datetime,
                    user_id,
                    file_path
                )
            )

        else:

            cursor.execute(
                """
                INSERT INTO file_integrity(
                    user_id,
                    file_path,
                    file_hash,
                    datetime
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    user_id,
                    file_path,
                    file_hash,
                    current_datetime
                )
            )

        conn.commit()
        return True

    except sqlite3.Error as e:

        print(e)
        return False

    finally:

        conn.close()


# Get previously saved file hash
def get_file_hash(user_id, file_path):

    conn, cursor = connect_db()

    if conn is None or cursor is None:
        return None

    try:

        cursor.execute(
            """
            SELECT file_hash
            FROM file_integrity
            WHERE user_id = ? AND file_path = ?
            """,
            (user_id, file_path)
        )

        result = cursor.fetchone()

        if result:
            return result[0]

        return None

    except sqlite3.Error as e:

        print(e)
        return None

    finally:

        conn.close()