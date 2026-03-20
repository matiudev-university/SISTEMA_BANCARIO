import sqlite3
import os
from db.schema import create_table
from db.seeds import seed_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db", "sistema_bancario.db")

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def db_init():
        # Creacion De Tablas
        create_table()

        # Insercion de Datos
        seed_data()

        print("✅ DB Inicializada y Datos Base Cargados!")
