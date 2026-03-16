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
            CREATE TABLE IF NOT EXISTS cliente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rut TEXT NOT NULL,
            nombres TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            fecha_nacimiento DATE,
            direccion TEXT NOT NULL,
            telefono TEXT NOT NULL,
            correo TEXT NOT NULL,
            password TEXT NOT NULL,
        )""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleado(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rut TEXT NOT NULL,
            nombres TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            fecha_nacimiento DATE,
            direccion TEXT NOT NULL,
            telefono TEXT NOT NULL,
            correo TEXT NOT NULL,
            password TEXT NOT NULL,
            id_sucursal TEXT NOT NULL,

            FOREIGN KEY(id_sucursal) REFERENCES 
        )""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cuentas(
                id_cuenta INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER NOT NULL,
                tipo_cuenta TEXT NOT NULL,
                saldo DECIMAL(10, 2) DEFAULT 0.0,
                estado TEXT DEFAULT 'Activa',
                       
                FOREIGN KEY (id_cliente) REFERENCES usuarios(id)
            )""")

        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tipo_cuenta(
                       )""")


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sucursarl(
                       )
            """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacciones(
                       )            
            """)

        connection.commit()
        print("✅ DB Inicializada con Exito!")

