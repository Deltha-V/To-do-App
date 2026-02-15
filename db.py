import sqlite3

DB_NAME = "todo.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                texto TEXT NOT NULL,
                hecha INTEGER NOT NULL DEFAULT 0
            )
        """)
        conn.commit()


def agregar_tarea(texto):
    texto = texto.strip()

    if not texto:
        return False

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tareas (texto, hecha) VALUES(?, ?)",
            (texto, 0)
        )

        conn.commit()

    return True
    

def get_tareas():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT id, texto, hecha FROM tareas")
        filas = cursor.fetchall()

        lista = []
        for fila in filas:
            tarea = {
                "id": fila[0],
                "texto": fila[1],
                "hecha": (fila[2] == 1)
            }
            lista.append(tarea)

        return lista

def get_tarea_por_id(id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT id, texto, hecha FROM tareas WHERE id = ?", (id,))
        fila = cursor.fetchone()

    if fila is None:
        return None

    tarea = {
        "id": fila[0],
        "texto": fila[1],
        "hecha": (fila[2] == 1)
    }

    return tarea


def get_tareas_pendientes():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT id, texto, hecha FROM tareas WHERE hecha = 0 ORDER BY id")
        filas = cursor.fetchall()

        lista = []
        for fila in filas:
            tarea = {
                "id" : fila[0],
                "texto" : fila[1],
                "hecha" : False
            }
            lista.append(tarea)
        
        return lista
    
def get_tareas_hechas():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT id, texto, hecha FROM tareas WHERE hecha = 1 ORDER BY id")
        filas = cursor.fetchall()

        lista = []
        for fila in filas:
            tarea = {
                "id" : fila[0],
                "texto" : fila[1],
                "hecha" : True
            }
            lista.append(tarea)

        return lista

def terminar_tarea(id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE tareas SET hecha = 1 WHERE id = ?",
            (id,)
        )

        conn.commit()

        return cursor.rowcount > 0

def eliminar_tarea(id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tareas WHERE id = ?",
            (id,)
        )

        conn.commit()

        return cursor.rowcount > 0
    
def editar_tarea(id, nuevo_texto):
    nuevo_texto = nuevo_texto.strip()

    if not nuevo_texto:
        return False
    
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE tareas SET texto = ? WHERE id = ?",
            (nuevo_texto, id)
        )

        conn.commit()

        return cursor.rowcount > 0
    
def eliminar_tarea(id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tareas WHERE id = ?",
            (id,)
        )

        conn.commit()

        return cursor.rowcount > 0