from db.db import get_connection

class Auth:
    
    @staticmethod
    def login(rut, password):
        with get_connection() as connection:
            cursor = connection.cursor()
            select_query = "SELECT * FROM clientes WHERE rut = ? and password = ?"

            cursor.execute(select_query, (rut, password))
            usuario = cursor.fetchone()

        return usuario