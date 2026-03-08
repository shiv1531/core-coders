import sqlite3

def get_connection():
    return sqlite3.connect("interview.db")


def create_table():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS interviews(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    mode TEXT,
    question TEXT,
    answer TEXT,
    score INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()
    conn.close()


def save_interview(username,mode,question,answer,score):

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""

    INSERT INTO interviews(username,mode,question,answer,score)

    VALUES(?,?,?,?,?)

    """,(username,mode,question,answer,score))

    conn.commit()
    conn.close()
