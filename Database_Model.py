import sqlite3 as sql
import sqlite3

def insertUser(username,password):
    con = sql.connect("pythonsqlite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()
    return True

def check_login(username,password):
    db = sql.connect("pythonsqlite.db")
    c = db.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    if c.fetchall():
        return True
    else:
        return False

def createtables():
    conn = sqlite3.connect('pythonsqlite.db')
    conn.execute("create table users (id integer primary key autoincrement, username text not null, password text not null);")
    conn.close()
    return True