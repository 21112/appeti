import sqlite3

conn = sqlite3.connect('dishes.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS dishe(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS desert(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT);
""")
conn.commit()

def add_dish(dish,signal):
    dish = str(dish)
    sap ="SELECT * FROM dishe WHERE name=?"
    c=cur.execute(sap,[dish])
    exist = c.fetchall()
    if len(exist)<1:
        add ="INSERT INTO dishe(name) VALUES(?)"
        cur.execute(add, [dish])
        signal.emit("OK!")
        conn.commit()
    else:
        signal.emit("Name is allready") 

def add_desert(desert,signal):    
    desert = str(desert)
    q = "SELECT * FROM desert WHERE name =?"
    c = cur.execute(q,[desert])
    exist = c.fetchall()
    if len(exist)<1:
        add ="INSERT INTO desert(name) VALUES(?)"
        cur.execute(add, [desert])
        signal.emit("OK!")
        conn.commit()
    else:
        signal.emit("Name is allready")   

def get_dish(signal):
    quert = "SELECT * FROM dishe ORDER BY RANDOM() LIMIT 1;"
    get_d = (cur.execute(quert)).fetchall()
    quert2 = "SELECT * FROM desert ORDER BY RANDOM() LIMIT 1;"
    get_des = (cur.execute(quert2)).fetchall()
    signal.emit(str(get_d[0][1]) +" и "+ str(get_des[0][1]))
    
    
