import sqlite3

DB_PATH = "db/sistema_bancario.db"

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db():
    with get_connection() as connection:
        cursor = connection.cursor()
        # Ejecutar Consultas

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rut TEXT NOT NULL,
            nombres TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            fecha_nacimiento DATE,
            direccion TEXT NOT NULL,
            telefono TEXT NOT NULL,
            correo TEXT NOT NULL
        )""")

        cursor.execute("""
                """)

        connection.commit()
        print("✅ DB Inicializada con Exito!")

