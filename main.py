import sqlite3

con = sqlite3.connect("db_test.db")
cur = con.cursor()
cur.execute("""
""")

con.close()
