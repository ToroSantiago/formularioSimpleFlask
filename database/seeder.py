import sqlite3 as sql

DB_PATH = "C:\\Users\\santi\\Desktop\\proyecto\\database\\usuario.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE usuarios (
        dni integer,
        nombre text,
        apellido text,
        email text,
        telefono text
    )""")
    conn.commit()
    conn.close()

def addUsuario():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()

    data = [
        (43477286, "Santiago Cesar", "Toro", "santiagotoro89@gmail.com", "2804569493")
    ]
    cursor.executemany("""INSERT INTO  usuarios VALUES (?,?,?,?,?)""", data)
    conn.commit()
    conn.close() 



if __name__ == "__main__":
    createDB()
    addUsuario()