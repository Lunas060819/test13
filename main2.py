import sqlite3

with sqlite3.connect("db_test.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS useres")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id = INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
    )
    """)

    cur.execute("""
    SELECT * FROM users
    """)

    print(cur.fetchall())

    cur.execute("""
        SELECT rowid, * FROM users
        """)

    print(cur.fetchall())
