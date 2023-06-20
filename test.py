import sqlite3

with sqlite3.connect("test.db") as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS user")
    cur.execute("""CREATE TABLE IF NOT EXISTS user (
                   id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   password NOT NULL DEFAULT 1 
    )""")

    # cur.execute("""INSERT INTO user VALUES  (1, 'Yunus', 5544)""")
    cur.execute("""INSERT INTO user (name, password) VALUES  ('Yusup', 1144)""")

    cur.execute("SELECT * FROM user")
    # print(cur.fetchall())
    # for i in cur:
    #     print(i)

    cur.execute("UPDATE user SET password = 1")
    cur.execute("SELECT * FROM user")
    # for i in cur:
    #     print(i)
#%%
    # cur.execute("DELETE FROM user WHERE name = 'Musa'")
    for i in cur:
        print(i)
