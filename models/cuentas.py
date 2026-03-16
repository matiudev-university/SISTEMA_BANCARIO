from db.db import get_connection

class Cuenta:
    def __init__(self, id_cliente, id_tipo_cuenta, saldo=0.0, estado="Activa", id_cuenta=None):
        self.id_cuenta = id_cuenta
        self.id_cliente = id_cliente
        self.id_tipo_cuenta = id_tipo_cuenta
        self.saldo = saldo
        self.estado = estado

    @staticmethod
    def crear_cuenta():
        print("\n=== APERTURA DE CUENTA ===")
        # Es ideal listar los clientes primero o pedir el ID
        id_cliente = input("Ingrese el ID del cliente dueño de la cuenta: ")
        tipo = input("Tipo de cuenta (Ahorro/Corriente): ")
        saldo_inicial = float(input("Monto de apertura: "))

        with get_connection() as connection:
            cursor = connection.cursor()
            query = """
                INSERT INTO cuentas (id_cliente, id_tipo_cuenta, saldo)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (id_cliente, tipo, saldo_inicial))
            connection.commit()
            print("✅ Cuenta creada exitosamente.")

    @staticmethod
    def consultar_saldo():
        print("\n=== CONSULTA DE SALDO ===")
        id_cta = input("Ingrese el ID de la cuenta: ")
        
        with get_connection() as connection:
            cursor = connection.cursor()
            query = "SELECT saldo, id_tipo_cuenta, estado FROM cuentas WHERE id = ?"
            cursor.execute(query, (id_cta,))
            row = cursor.fetchone()
            
            if row:
                print(f"\nCuenta N°: {id_cta} | Tipo: {row[1]}")
                print(f"Estado: {row[2]}")
                print(f"Saldo Actual: ${row[0]}")
            else:
                print("❌ Cuenta no encontrada.")