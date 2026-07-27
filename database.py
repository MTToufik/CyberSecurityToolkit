# import sqlite3 library
import sqlite3



db_name = "database/security.db"

# build a function to connect to the database

def connect_db():

    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        print(f"Connected successfully")
        return conn, cursor
    except sqlite3.Error as e:
        print("Database connection error")
        print(e)
        return None, None
    

# build a function to create tables in the database

def create_tables():
    conn, cursor = connect_db()
    # if conn is not None and cursor is not None:
    #     return conn, cursor
    if conn is None or cursor is None:
        return 
    
    
    # table for users
    try:
      cursor.execute("""CREATE TABLE IF NOT EXISTS users(

                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL UNIQUE,
                   email TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL
                   )""")
    
    

      # history table for user login attempts
      
      cursor.execute("""CREATE TABLE IF NOT EXISTS history(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER NOT NULL,
                  tool_name TEXT NOT NULL,
                  result TEXT NOT NULL,
                  datetime TEXT NOT NULL
                  )""")
      # save the changes to the database
      conn.commit()

    except sqlite3.Error as e:
         print(f"Error creating tables: {e}")
    finally:
        # close the database connection
        conn.close()
        print("Database connection closed after creating tables.")


# function for insert user data

def insert_user(username, email, password):

    conn, cursor = connect_db()

    if conn is None or cursor is None:
        return False
    
    try:
        cursor.execute(
            """
            INSERT INTO users(username,email,password)
            VALUES (?, ?, ?)
            """,
            # pass the value here (?)
            (username, email,password)
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

       