import sqlite3

with sqlite3.connect("db_test.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS useres")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
    )
    """)


    cur.execute("""UPDATE users SET score = 0""")
    cur.execute("""UPDATE users SET score = 10 WHERE rowid = 1""")
    cur.execute("""UPDATE users SET score + 10 WHERE sex = 2""")
    cur.execute("""UPDATE users SET score + 10 WHERE LIKE 'www'""")

    # % любое продолжение строки
    # _ любой символ
    cur.execute("""UPDATE users SET score + 10 WHERE LIKE 'w%'""")
    cur.execute("""UPDATE users SET score + 10 WHERE LIKE 'w_w'""")
    cur.execute("""UPDATE users SET score = 700 WHERE LIKE 'w_w%'""")

    cur.execute("""UPDATE users SET score = 800 WHERE old > 40""")


    cur.execute("""DELETE FROM users WHERE rowid IN (2, 5)""")
