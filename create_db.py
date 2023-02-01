import sqlite3

con = sqlite3.connect("taskdb.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT ,done BOOLEAN)
""")
con.commit()

cur = con.cursor()
cur.execute("""
INSERT INTO tasks(id, content,done) VALUES('0','primo task',false)
""")
con.commit()