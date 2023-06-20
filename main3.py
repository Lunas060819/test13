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


    print(cur.fetchall())

    cur.execute("""INSERT INTO users VALUES ('WWW', 1, 19, 1000)""")

    cur.execute("""INSERT INTO users (name, old, score) VALUES ('SSS', 32, 200)""")

    cur.execute("""SELECT name, old, score FROM users""")
    print(cur.fetchall())

    cur.execute("""
       SELECT * FROM users
       """)

    print(cur.fetchall())

    cur.execute("""
            SELECT rowid, * FROM users
            """)


    cur.execute("""SELECT * FROM users WHERE score < 1000""")
    print(cur.fetchall())

    cur.execute("""SELECT * FROM users WHERE score BETWEEN 500 AND 1000""")  # В ИНТЕРВАЛЕ ОТ 500 ДО 1000


    cur.execute("""SELECT * FROM users WHERE old > 20 AND score < 1000""")

    cur.execute("""SELECT * FROM users WHERE old IN (19, 32) AND score <= 1000""")

    cur.execute("""SELECT * FROM users WHERE old IN (19, 32) AND score <= 1000 OR sex == 1""")

    cur.execute("""SELECT * FROM users WHERE old IN (19, 32) AND (score <= 1000 OR sex == 1)""")


    cur.execute("""SELECT * FROM users WHERE old IN (19, 32) AND (score <= 1000 OR sex == 1)
                   ORDER BY old
                   """)
    # по убыванию
    cur.execute("""SELECT * FROM users WHERE old IN (19, 32) AND (score <= 1000 OR sex == 1)
                       ORDER BY old DESC  
                       """)

    cur.execute("""SELECT * FROM users WHERE old IN (19, 32) AND (score <= 1000 OR sex == 1)
                           ORDER BY old ASC
                           """)

    cur.execute("""SELECT * FROM users WHERE old IN (19, 32) AND (score <= 1000 OR sex == 1)
                           ORDER BY old ASC 
                           LIMIT 2
                           """)

    # 1 пропустить, показать след. 2
    cur.execute("""SELECT * FROM users WHERE old IN (19, 32) AND (score <= 1000 OR sex == 1)
                               ORDER BY old ASC 
                               LIMIT 1 OFFSET 2  
                               """)


    cur.execute("""SELECT * FROM users WHERE old IN (19, 32) AND (score <= 1000 OR sex == 1)
                               ORDER BY old ASC 
                               LIMIT 1, 2
                               """)

    res = cur.fetchall()
    print(res)

    for res in cur:  # предпочтительнее когда число записей очень много
        print(res)

    res2 = cur.fetchone()
    res3 = cur.fetchmany(2)
