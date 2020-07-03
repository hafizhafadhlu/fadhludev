import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date TEXT , earnings INTEGER , exercise TEXT , study TEXT , game TEXT , python TEXT)")
    conn.commit()
    conn.close

def insert(date , earnings , exercise , study , game , python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)" , (date , earnings , exercise , study , game , python))
    conn.commit()
    conn.close

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?" , (id,))
    conn.commit()
    conn.close

def search(date='' , earnings='' , exercise='' , study='' , game='' , python=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earnings=? OR exercise=? OR study=? OR game=? OR python=?" , (date , earnings , exercise , study , game , python))
    rows = cur.fetchall()
    conn.commit()
    conn.close
    return rows

connect()
# insert('3-2-2020' , 50000 , '-' , '-' , 'YES' , 'did')
# # print(view())
# delete(2)
# delete(3)
# print(view())
# x = search(earnings=50000)
# print(x)