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
            CREATE TABLE IF NOT EXISTS usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rut TEXT UNIQUE NOT NULL,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                fecha_nacimiento DATE,
                direccion TEXT,
                telefono TEXT,
                correo TEXT,
                password TEXT NOT NULL
        )""")

        cursor.execute("""
           CREATE TABLE IF NOT EXISTS cliente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
    
            FOREIGN KEY(usuario_id) REFERENCES usuario(id)
        )""")

        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sucursal(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono TEXT
        )""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleado(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            id_sucursal INTEGER,

            FOREIGN KEY(usuario_id) REFERENCES usuario(id)
            FOREIGN KEY(id_sucursal) REFERENCES sucursal(id)
        )""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gerente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            id_sucursal INTEGER,

            FOREIGN KEY(usuario_id) REFERENCES usuario(id)
            FOREIGN KEY(id_sucursal) REFERENCES sucursal(id)
        )""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tipo_cuenta(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_cuenta TEXT NOT NULL
        )""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cuentas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            id_tipo_cuenta INTEGER NOT NULL,
            saldo DECIMAL(10, 2) DEFAULT 0.0,
            estado TEXT DEFAULT 'Activa',
                       
            FOREIGN KEY (id_cliente) REFERENCES cliente(id),
            FOREIGN KEY (id_tipo_cuenta) REFERENCES tipo_cuenta(id)
        )""")
        
        # cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS transacciones(
        #                )            
        #     """)

        connection.commit()
        print("✅ DB Inicializada con Exito!")

